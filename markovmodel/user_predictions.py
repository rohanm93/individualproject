from __future__ import division
import csv
import markov
import cluster
from datetime import datetime
import time

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
	elif ("Bautista" in player1):
		return "bautistaagut.csv"
	elif ("Dolgopolov" in player1):
		return "dolgopolov.csv"
	elif ("Fognini" in player1):
		return "fognini.csv"
	elif ("Janowicz" in player1):
		return "janowicz.csv"
	elif ("Kohlschreiber" in player1):
		return "kohlschreiber.csv"
	elif ("Feliciano Lopez" in player1):
		return "lopez.csv"
	elif ("Gilles Simon" in player1):
		return "simon.csv"

def predictions(player1, player2):
	p1_filename = get_filename(player1)
	p1_file_path = "dataset/sorted/10_clusters/"+ str(p1_filename)
	p1_reader = csv.reader(open(p1_file_path), delimiter=',')
	p1_reader.next() # skip headers
	player_list = []
	cluster_list = []
	for row in p1_reader:
		if player2 in row[2]:
			cluster_list.append(row[11])
		player_list.append(row)
	print cluster_list
	spw_value,total_spws = calculate_spw(cluster_list, player_list, player2)
	return (spw_value, total_spws)

def calculate_spw(cluster_list, player_list, player2):
	difference_a_c = 0
	difference_spw_rpw_p1 = 0
	normalisation_counter = 0
	players_in_p2_profile = get_similar_profile_players(player2)
	for rec in player_list: #of form [p2serve, p2return, p2, odds, winner, date, tournament, t_round, p1, outlier, id, cluster]
		#if we're playing against a player which is the same cluster also set same_profile to 1
		same_profile = 0
		if any(x in rec[2] for x in players_in_p2_profile):
			same_profile = 1
		if (rec[11] in cluster_list) or same_profile:
			swp_p2 = float(rec[0])
			rwp_p2 = float(rec[1])
			print player2 + " is similar to "+rec[2]+" " +str(swp_p2) + ", "+ str(rwp_p2)
			#manipulating p2 values to p1 & converting to decimals
			#below is the same as spw(A,Ci)-(1-rpw(A,Ci))
			difference_spw_rpw_p1 = (100.0-rwp_p2-swp_p2)/100
			difference_a_c += difference_spw_rpw_p1
			normalisation_counter+=1
	# only take their last fixture head to head, not all of them
	'''
	# add people in other player2's clusters
	# eg. fed vs nadal, for fed, people in nadals cluster, and other clusters 
	# that those same people in nadal's cluster were in. only take most rec game
	d = {}
	for rec in player_list:
		if (rec[11] not in cluster_name) and (rec not in added):
			if rec[2] in other_players:
				swp_p2 = float(rec[0])
				rwp_p2 = float(rec[1])
				#manipulating p2 values to p1 & converting to decimals
				#below is the same as spw(A,Ci)-(1-rpw(A,Ci))
				difference_spw_rpw_p1 = (100.0-rwp_p2-swp_p2)/100
				d[rec[2]] = difference_spw_rpw_p1
	for key, value in d.iteritems():
		difference_a_c += value
		normalisation_counter+=1
	'''
	return (difference_a_c, normalisation_counter)

def get_similar_profile_players(player2):
	f = open("profiles_clustered_9clusters.csv")
	profiles_clustered = csv.DictReader(f)
	cluster="cluster_000" #error
	for player in profiles_clustered:
		if (player["player"].split()[-1] == player2.split()[-1]):
			cluster = player["cluster"]
	if cluster=="cluster_000":
		print "ERROR", player2
	f.seek(0)
	#note: this takes into account the current p2 player as well
	list_of_players = []
	for player in profiles_clustered:
		if player["cluster"]==cluster:
			list_of_players.append(player["player"].split()[-1])
	return list_of_players

def match_up(player1, player2):
	spw_p1, counter_p1 = predictions(player1,player2)
	spw_p2, counter_p2 = predictions(player2,player1)
	# ask if its a five setter tournament
	five_setter = 1
	#normalizing values
	avg_p1spw = spw_p1/counter_p1
	avg_p2spw = spw_p2/counter_p2
	delta_a_b = avg_p1spw - avg_p2spw
	p1_win_probability = markov.match_win_probability_5(0.6+delta_a_b,(1-0.6))+markov.match_win_probability_5(0.6,(1-(0.6-delta_a_b)))
	p1_win_probability = p1_win_probability/2
	p2_win_probability = 1-p1_win_probability
	predicted_odds_p1 = 1/p1_win_probability
	predicted_odds_p2 = 1/p2_win_probability
	print str(avg_p1spw) + ", " + str(avg_p2spw)
	print "In a match up between " + player1 + " and " + player2 + " on " + str(time.strftime("%d/%m/%Y"))
	print "Player 1 win probability: " + str(p1_win_probability*100) + "%"
	print "Player 2 win probability: " + str(p2_win_probability*100) + "%"
	print "Only bet on Player 1 if the odds>$"+str(predicted_odds_p1)
	print "Only bet on Player 2 if the odds>$"+str(predicted_odds_p2)

match_up("Anderson", "Tsonga")