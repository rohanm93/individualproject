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
	reader1 = csv.reader(open("outliers_fixed/almagro.csv"), delimiter=",")
	headers = reader1.next()
	reader = csv.reader(open("fixtures.csv"), delimiter=",")
	data = sorted(reader, key = lambda row: datetime.strptime(row[5], "%b %d %Y"))
	with open("fixtures-datesorted.csv", "wb") as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow(headers)
		writer.writerows(data)

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
sort_dataset_by_date()
#get_info_serve_net("Berdych")

