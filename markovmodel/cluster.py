from __future__ import division
import csv
import markov
from datetime import datetime
import scipy
from scipy.cluster.vq import kmeans2


def cluster():
	x = [[67,36],[34,99],[35,98],[70,40]]
	centroids, labels = kmeans2(scipy.array(x), 2)
	#print centroids
	print labels
	print labels[0]
	print labels[1]

def cluster_spw_rpw(list_of_recs):
	number_of_clusters = 8
	only_serve_return = []
	for rec in list_of_recs:
		only_serve_return.append(rec[0],rec[1])
	centroids, labels = kmeans2(scipy.array(only_serve_return),8)
	

cluster()