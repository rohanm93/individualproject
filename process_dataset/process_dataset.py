# this code creates a player's profile
from __future__ import division
import csv

input_file = csv.DictReader(open("djokovic_stats.csv"))

#finds average net approaches and average first serve
def get_info_serve_net(player_name):
	total_net_approaches = 0
	total_serve_speed = 0
	count_net = 0
	count_serve = 0
	for row in input_file:
		net_approaches = 0
		serve_speed = 0
		player1 = row["player1"]
		player2 = row["player2"]
		if (player1==player_name):
			if row["p1AverageFirstServeSpeed"] == "":
				serve_speed = 0
			else:
				serve_speed = int(float(row["p1AverageFirstServeSpeed"]))
			if row["p1NetApproaches"] == "":
				net_approaches = 0
			else:
				net_approaches = int(float(row["p1NetApproaches"]))
		if (player2==player_name):
			if row["p2AverageFirstServeSpeed"] == "":
				serve_speed = 0
			else:
				serve_speed = int(float(row["p2AverageFirstServeSpeed"]))
			if row["p2NetApproaches"] == "":
				net_approaches = 0
			else:
				net_approaches = int(float(row["p2NetApproaches"]))
		if (net_approaches>0):
			total_net_approaches+=net_approaches
			count_net+=1
		if (serve_speed>0):
			total_serve_speed+=serve_speed
			count_serve+=1
	print player_name
	print total_net_approaches/count_net
	print total_serve_speed/count_serve

get_info_serve_net("Novak Djokovic")

