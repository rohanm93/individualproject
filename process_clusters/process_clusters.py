#this file contains code to find the difference in serve percentages for one player over the other

import csv



def find_clusters_of_player(player_name):
	input_file = csv.DictReader(open("federer_clusters.csv"))
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

find_clusters_of_player("Novak Djokovic")


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
        			#opponent player found
'''
