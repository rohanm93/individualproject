# this code creates a player's profile
from __future__ import division
from datetime import datetime
import csv

#input_file = csv.DictReader(open("k-means/almagro.csv"))

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
		if (player_name in player1):
			if row["p1AverageFirstServeSpeed"] == "":
				serve_speed = 0
			else:
				serve_speed = int(float(row["p1AverageFirstServeSpeed"]))
			if row["p1NetApproaches"] == "":
				net_approaches = 0
			else:
				net_approaches = int(float(row["p1NetApproaches"]))
		if (player_name in player2):
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
	if not count_net==0:
		print total_net_approaches/count_net
	print total_serve_speed/count_serve


def sort_dataset_by_date():
	reader = csv.reader(open("k-means/youzhny.csv"), delimiter=",")
	headers = reader.next()
	data = sorted(reader, key = lambda row: datetime.strptime(row[6], "%b %d %Y"))
	with open("k-means_datesorted/youzhny.csv", "wb") as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow(headers)
		writer.writerows(data)

sort_dataset_by_date()
#get_info_serve_net("Berdych")

