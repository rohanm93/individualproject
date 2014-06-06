from __future__ import division
import csv
import markov


def get_filename(player1):
	if ("Almagro" in player1):
		return "almagro.csv"
	elif ("Anderson" in player1):
		return "anderson.csv"
	elif ("Berdych" in player1):
		return "berdych.csv"
	elif ("Chardy" in player1):
		return "chardy.csv"
	elif ("Cilic" in player1):
		return "cilic.csv"
	elif ("Potro" in player1):
		return "delpotro.csv"
	elif ("Dimitrov" in player1):
		return "dimitrov.csv"
	elif ("Djokovic" in player1):
		return "djokovic.csv"
	elif ("Federer" in player1):
		return "federer.csv"
	elif ("Ferrer" in player1):
		return "ferrer.csv"
	elif ("Gasquet" in player1):
		return "gasquet.csv"
	elif ("Gulbis" in player1):
		return "gulbis.csv"
	elif ("Haas" in player1):
		return "haas.csv"
	elif ("Hewitt" in player1):
		return "hewitt.csv"
	elif ("Isner" in player1):
		return "isner.csv"
	elif ("Murray" in player1):
		return "murray.csv"
	elif ("Monfils" in player1):
		return "monfils.csv"
	elif ("Nadal" in player1):
		return "nadal.csv"
	elif ("Nishikori" in player1):
		return "nishikori.csv"
	elif ("Raonic" in player1):
		return "raonic.csv"
	elif ("Robredo" in player1):
		return "robredo.csv"
	elif ("Seppi" in player1):
		return "seppi.csv"
	elif ("Tsonga" in player1):
		return "tsonga.csv"
	elif ("Verdasco" in player1):
		return "verdasco.csv"
	elif ("Wawrinka" in player1):
		return "wawrinka.csv"
	elif ("Youzhny" in player1):
		return "youzhny.csv"

def predictions():
	input_file = csv.reader(open("fixtures.csv"), delimiter=',')
	fixtures_with_spw = csv.writer(open("fixtures_with_spw.csv", "wb"), delimiter=',')
	#skip first 60 matches (dont predict these fixtures), only predict matches from nov 2012 onwards
	for i in range(60):
		input_file.next()
	for row in input_file:
		#player1 = row["player1"]
		player1 = row[8]
		p2Serve = row[0]
		p2ReturnPointsWon = row[1]
		odds = row[3]
		winner = row[4]
		player2 = row[2]
		# error case since haas in Haase
		if player2.split()[-1]=="Haase" or player1.split()[-1]=="Haase":
			continue
		filename = get_filename(player1)
		file_path = "dataset/sorted/"+ str(filename)
		reader = csv.reader(open(file_path), delimiter=',')
		player_list = []
		player1_cluster = "cluster_000"
		for player_row in reader:
			if (player1==player_row[8] and float(p2Serve)==float(player_row[0]) and float(p2ReturnPointsWon)==float(player_row[1]) and odds==player_row[3] and player2==player_row[2]):
				# reached the record so stop
				# use data so far to calculate spw
				#player1_cluster = player_row[11]
				break
			else:
				#also add the case if a player is in multiple clusters
				#average them out for both players
				if (player2==player_row[2]):
					player1_cluster = player_row[11]
				player_list.append(player_row)	
		
		if not player_list:
			print "no one before player1 or ERROR"
			continue
		#at this point player_list contains all required data to do spw calculation for Player 1 - the same needs to be done for player 2
		#important note - this just takes into account player 2's most recent cluster. ie. Haas vs Djokovic, will only take into account for Djokovic the cluster of their most recent match, say Djokovic is in multiple clusters
		spw_value,total_spws = calculate_spw(player1_cluster, player_list, player2)
		row.append(spw_value)
		row.append(total_spws)
		fixtures_with_spw.writerow(row)

def calculate_spw(cluster_name, player_list, player2):
	difference_a_c = 0
	difference_spw_rpw_p1 = 0
	normalisation_counter = 0
	players_in_p2_profile = get_similar_profile_players(player2)
	for rec in player_list: #of form [p2serve, p2return, p2, odds, winner, date, tournament, t_round, p1, outlier, id, cluster]
		#if we're playing against a player which is the same cluster also set variable to 1
		same_profile = 0
		if any(x in rec[2] for x in players_in_p2_profile):
			same_profile = 1
		if cluster_name == rec[11] or same_profile:
			swp_p2 = float(rec[0])
			rwp_p2 = float(rec[1])
			#manipulating p2 values to p1 & converting to decimals
			#below is the same as spw(A,Ci)-(1-rpw(A,Ci))
			difference_spw_rpw_p1 = (100.0-rwp_p2-swp_p2)/100
			difference_a_c += difference_spw_rpw_p1
			normalisation_counter+=1
	return (difference_a_c, normalisation_counter)

def get_similar_profile_players(player2):
	f = open("profiles_clustered.csv")
	profiles_clustered = csv.DictReader(f)
	cluster="cluster_10" #error
	for player in profiles_clustered:
		if (player["player"].split()[-1] == player2.split()[-1]):
			cluster = player["cluster"]
	if cluster=="cluster_10":
		print "ERROR", player2
	f.seek(0)
	#note: this takes into account the current p2 player as well
	list_of_players = []
	for player in profiles_clustered:
		if player["cluster"]==cluster:
			list_of_players.append(player["player"].split()[-1])
	return list_of_players

def get_fixtures_to_predict():
	players_list = ["Almagro", "Kevin Anderson", "Berdych", "Jeremy Chardy", "Cilic", "Potro", "Grigor Dimitrov", "Djokovic", "Federer", "David Ferrer", "Gasquet", "Gulbis", "Haas", "Hewitt", "Isner", "Monfils", "Murray", "Nadal", "Nishikori", "Raonic", "Robredo", "Seppi", "Tsonga", "Verdasco", "Wawrinka", "Youzhny"]
	filepath_list = ["almagro", "anderson", "berdych", "chardy", "cilic", "delpotro", "dimitrov", "djokovic", "federer", "ferrer", "gasquet", "gulbis", "haas", "hewitt", "isner", "monfils", "murray", "nadal", "nishikori", "raonic", "robredo", "seppi", "tsonga", "verdasco", "wawrinka", "youzhny"]
	filepath_string = "dataset/sorted/"
	all_fixtures = []
	output = open("fixtures.csv", "wb")
	writer = csv.writer(output, delimiter=',')
	for fp in filepath_list:
		reader = csv.reader(open(filepath_string+fp+".csv"), delimiter=',')
		headers = reader.next()
		for rec in reader:
			if any(x in rec[2] for x in players_list):
				writer.writerow(rec)

def simulate_bets():
	fixtures = csv.DictReader(open("final_fixtures.csv"))
	roi = 0
	matches_bet_on = 0
	correct_bets = 0
	wrong_bets = 0
	for fixture in fixtures:
		delta_a_b = 0
		winner = -1
		five_setter=0
		if (fixture["winner"]==fixture["player1"]):
			winner=1
		elif (fixture["winner"]==fixture["player2"]):
			winner=2
		if winner<0:
			print "ERROR, DOES NOT READ PLAYER 1 AND 2 CORRECTLY"
		# remove the $ symbol and convert to float
		market_odds_p1 = float(fixture["p1odds"][1:])
		market_odds_p2 = float(fixture["p2odds"][1:])
		tournament = fixture["tournament"]
		# if grand slam or davis cup, its a 5 setter match
		if "Slam" in tournament:
			five_setter = 1
		p1spw = float(fixture["p1spw"])
		p2spw = float(fixture["p2spw"])
		p1_spwcount = float(fixture["p1_spwcount"])
		p2_spwcount = float(fixture["p2_spwcount"])
		if (p1_spwcount==0 or p2_spwcount==0):
			#dont bet because there isnt enough clustering info
			continue
		#normalizing values
		avg_p1spw = p1spw/p1_spwcount
		avg_p2spw = p2spw/p2_spwcount
		delta_a_b = avg_p1spw - avg_p2spw
		delta_b_a = avg_p2spw - avg_p1spw

		if (five_setter):
			#use five setter formula
			p1_win_probability = markov.match_win_probability_5(0.6+delta_a_b,(1-0.6))+markov.match_win_probability_5(0.6,(1-(0.6-delta_a_b)))
			p1_win_probability = p1_win_probability/2
			p2_win_probability = 1-p1_win_probability
		else:
			#use three sets formula (default)
			p1_win_probability = markov.match_win_probability_3(0.6+delta_a_b,(1-0.6))+markov.match_win_probability_3(0.6,(1-(0.6-delta_a_b)))
			p1_win_probability = p1_win_probability/2
			p2_win_probability = 1-p1_win_probability

		predicted_odds_p1 = 1/p1_win_probability
		predicted_odds_p2 = 1/p2_win_probability

		#betted = 1 if bet on player 1, =2 if bet on player 2
		betted = -1

		if (market_odds_p1>predicted_odds_p1 and predicted_odds_p1<2):
			# bet pound on p1
			betted = 1
			matches_bet_on +=1
		elif (market_odds_p2>predicted_odds_p2 and predicted_odds_p2<2):
			# bet pound on p2
			betted = 2
			matches_bet_on +=1
		if betted<0:
			#print "NO BET"
			continue

		if (betted==1 and winner==1):
			roi+=(market_odds_p1-1)
			correct_bets+=1
		elif (betted==2 and winner==2):
			roi+=(market_odds_p2-1)
			correct_bets+=1
		elif (betted==1 and winner==2):
			print fixture["date"] + "  "+ fixture["player1"] + " vs " + fixture["player2"] + ", bet on :"+ fixture["player1"]
			roi-=1
			wrong_bets+=1
		elif (betted==2 and winner==1):
			print fixture["date"] + "  "+ fixture["player1"] + " vs " + fixture["player2"] + ", bet on :"+ fixture["player2"]
			roi-=1
			wrong_bets+=1
	print "$"+str(roi)
	print "Bet on " + str(matches_bet_on) + " matches"
	print "Correct bets:" + str(correct_bets)
	print "Incorrect bets:" + str(wrong_bets)

		# normalize the p1spw and p2spw using the p1_spwcount and p2_spwcount
		# get difference (triangle)
		# predict the probability of winning using methods in markov.py
		# if  predicted odds > market odds then bet a pound; check for both p1 and p2
		# check winner; if winner is p1 and bet on p1 then add winnings
		# if loss then subtract from total roi

#def predict_matchup(player1, player2):


# odds = 1/p where p is the probability of a player winning a match 

#get_fixtures_to_predict()
#predictions()
simulate_bets()
#print get_similar_profile_players("Milos Raonic")