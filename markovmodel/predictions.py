from __future__ import division
import csv

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
	#skip first 60 matches, from start of 2013
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
		filename = get_filename(player1)
		file_path = "dataset/"+ str(filename)
		reader = csv.reader(open(file_path), delimiter=',')
		player_list = []
		for player_row in reader:
			if (player1==player_row[8] and float(p2Serve)==float(player_row[0]) and float(p2ReturnPointsWon)==float(player_row[1]) and odds==player_row[3] and player2==player_row[2]):
				# reached the record so stop
				# use data so far to calculate spw
				player1_cluster = player_row[11]
				break
			else:
				player_list.append(player_row)
		
		if not player_list:
			print "no one before player1 or ERROR"
			continue
		#at this point player_list contains all required data to do spw calculation for Player 1 - the same needs to be done for player 2
		#important note - this just takes into account player 2's most recent cluster. ie. Haas vs Djokovic, will only take into account for Djokovic the cluster of their most recent match, say Djokovic is in multiple clusters
		spw_value = calculate_spw(player1_cluster, player_list)
		row.append(spw_value)
		fixtures_with_spw.writerow(row)

def calculate_spw(cluster_name, player_list):
	difference_a_c = 0
	difference_spw_rpw_p1 = 0
	for rec in player_list: #of form [p2serve, p2return, p2, odds, winner, date, tournament, t_round, p1, outlier, id, cluster]
		if cluster_name == rec[11]:
			swp_p2 = float(rec[0])
			rwp_p2 = float(rec[1])
			#manipulating p2 values to p1 & converting to decimals
			#below is the same as spw(A,Ci)-(1-rpw(A,Ci))
			difference_spw_rpw_p1 = (100.0-rwp_p2-swp_p2)/100
			difference_a_c += difference_spw_rpw_p1
	return difference_a_c

def get_fixtures_to_predict():
	players_list = ["Almagro", "Kevin Anderson", "Berdych", "Jeremy Chardy", "Cilic", "Potro", "Grigor Dimitrov", "Djokovic", "Federer", "David Ferrer", "Gasquet", "Gulbis", "Haas", "Hewitt", "Isner", "Monfils", "Nadal", "Nishikori", "Raonic", "Robredo", "Seppi", "Tsonga", "Verdasco", "Wawrinka", "Youzhny"]
	filepath_list = ["almagro", "anderson", "berdych", "chardy", "cilic", "delpotro", "dimitrov", "djokovic", "federer", "ferrer", "gasquet", "gulbis", "haas", "hewitt", "isner", "monfils", "nadal", "nishikori", "raonic", "robredo", "seppi", "tsonga", "verdasco", "wawrinka", "youzhny"]
	filepath_string = "outliers_fixed/"
	all_fixtures = []
	output = open("fixtures.csv", "wb")
	writer = csv.writer(output, delimiter=',')
	for fp in filepath_list:
		reader = csv.reader(open(filepath_string+fp+".csv"), delimiter=',')
		headers = reader.next()
		for rec in reader:
			if any(x in rec[2] for x in players_list):
				writer.writerow(rec)


		#data = list(list(rec) for rec in reader)


#get_fixtures_to_predict()
#get_info_serve_net("Berdych")

predictions()