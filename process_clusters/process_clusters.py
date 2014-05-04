#this file contains code to find the difference in serve percentages for one player over the other

import csv

input_file = csv.DictReader(open("federer_clusters.csv"))
# notation/formula implemented:
# ABi =(spw(A,Ci)-(1-rpw(A,Ci))) - (spw(B,Ci)-(1-rpw(B,Ci)))
# ABi = Difference(A,Ci)         - Difference(B,Ci)
difference_a_c = 0

def find_clusters_of_player(player_name):
	list_of_clusters = []
	for row in input_file:
		#player2 = str(row["player2"])
		player2 = row["player2"]
		if player_name == player2:
			cluster = row["cluster"]
			list_of_clusters.append(cluster)
		# if only want the first cluster found, use the break
		# break
	print list_of_clusters

def find_players_in_cluster(cluster_name):
	global difference_a_c
	for row in input_file:
		cluster = row["cluster"]
		if cluster_name == cluster:
			player = row["player2"]
			swp_p2 = float(row["p2PointWonOnServe"])
			rwp_p2 = float(row["p2ReturnPointWonPercentage"])
			#manipulating p2 values to p1 & converting to decimals
			#below is the same as spw(A,Ci)-(1-rpw(A,Ci))
			difference_spw_rpw_p1 = (100.0-rwp_p2-swp_p2)/100
			print player + ", " + cluster + ", " + str(difference_spw_rpw_p1)
			difference_a_c += difference_spw_rpw_p1

#find_clusters_of_player("Novak Djokovic")
find_players_in_cluster("cluster_1")


'''	with open('federer_clusters.csv', 'rb') as f:
    	reader = csv.reader(f, delimiter=',')
    	rownum = 0
    	for row in reader:
    		if rownum==0:
    			header = row #save header rw
    		else:
    			colnum = 0
    			for col in row:

        	for field in row:
        		if field==player_name:
        			#opponent player foundr
'''
