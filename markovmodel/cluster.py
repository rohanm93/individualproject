from __future__ import division
import csv
import markov
from datetime import datetime
import scipy
from scipy.cluster.vq import kmeans2
import Pycluster
import math

def cluster():
	x = [[76.0,32.0],[63.0,99],[63.0,39],[63.0,29]]
	#labels, error, nfound = Pycluster.kcluster(scipy.array(x), 20)
	#print centroids
	k = get_k_value(x)
	print k
	labels, error, nfound = Pycluster.kcluster(scipy.array(x),k)
	print labels[0]

def cluster_spw_rpw(list_of_recs):
	number_of_clusters = 8
	only_serve_return = []
	i = 0
	if list_of_recs==[]:
		print "ERRROR"
	for rec in list_of_recs:
		only_serve_return.append([float(rec[0]),float(rec[1])])
		i+=1
	k = get_k_value(only_serve_return)
	print only_serve_return
	labels, error, nfound = Pycluster.kcluster(scipy.array(only_serve_return), k)
	return labels

#currently just using rule of thumb technique
def get_k_value(only_serve_return):
	n = len(only_serve_return)
	k = math.sqrt(n/2)
	return int(math.ceil(k))

#cluster()