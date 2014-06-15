from __future__ import division
import csv
import markov
from datetime import datetime
import scipy
from scipy.cluster.vq import kmeans2
import Pycluster
import math

def cluster():
	x = [[76.0,32.0],[63.0,40.0],[70.0,30.0],[64.0,45.0]]
	k = 2
	labels, error, nfound = Pycluster.kcluster(scipy.array(x),k)
	print "Input data:"
	print "   spw " + "  rpw"
	j = 1
	for i in x:
		print str(j)+") "+str(i[0]) + "  " + str(i[1])
		j +=1
	print " "
	print "clusters: " + str(labels)

def cluster_spw_rpw(list_of_recs):
	number_of_clusters = 8
	only_serve_return = []
	if list_of_recs==[]:
		print "ERRROR"
	for rec in list_of_recs:
		only_serve_return.append([float(rec[0]),float(rec[1])])
	k = get_k_value(only_serve_return)
	labels, error, nfound = Pycluster.kcluster(scipy.array(only_serve_return), k)
	return labels

#currently just using rule of thumb technique
def get_k_value(only_serve_return):
	n = len(only_serve_return)
	k = math.sqrt(n/2)
	return int(math.ceil(k))

#cluster()