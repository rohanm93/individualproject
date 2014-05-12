from __future__ import division
import math
import numpy
#import division loads the division module so no integer rounding

matrix_A_tiebreak = (numpy.matrix([[1,3,0,4,0,0],
									[3,3,1,4,0,0],
									[4,4,0,3,1,0],
									[6,3,2,4,0,0],
									[16,4,1,3,1,0],
									[6,5,0,2,2,0],
									[10,2,3,5,0,0],
									[40,3,2,4,1,0],
									[30,4,1,3,2,0],
									[4,5,0,2,3,0],
									[5,1,4,6,0,0],
									[50,2,3,5,1,0],
									[100,3,2,4,2,0],
									[50,4,1,3,3,0],
									[5,5,0,2,4,0],
									[1,1,5,6,0,0],
									[30,2,4,5,1,0],
									[150,3,3,4,2,0],
									[200,4,2,3,3,0],
									[75,5,1,2,4,0],
									[6,6,0,1,5,0],
									[1,0,6,6,0,1],
									[36,1,5,5,1,1],
									[225,2,4,4,2,1],
									[400,3,3,3,3,1],
									[225,4,2,2,4,1],
									[36,5,1,1,5,1],
									[1,6,0,0,6,1]]))

def game_win_probability(p):
	#p is probability server wins a point (on his serve)
	top_fraction = 10*math.pow(p, 2)
	bottom_fraction = 1-(2*p*(1-p))
	computed_fraction = top_fraction/bottom_fraction
	inside = 15-4*p - computed_fraction
	result = math.pow(p,4) * inside
	return result

def tiebreak_win_probability(p,q):
	#p is probability of winning point serve 
	#q is probability of winning point return 
	total_probability = 0
	for i in range(28):
		first = matrix_A_tiebreak[i,0]
		second = math.pow(p,matrix_A_tiebreak[i,1])
		third = math.pow(1-p,matrix_A_tiebreak[i,2])
		fourth = math.pow(q,matrix_A_tiebreak[i,3])
		fifth = math.pow(1-q,matrix_A_tiebreak[i,4])
		d_pq = d_p_q(p,q)
		sixth = math.pow(d_pq,matrix_A_tiebreak[i,5])
		result = first*second*third*fourth*fifth*sixth
		total_probability = total_probability + result
	return total_probability
#matrix_A_tiebreak[row, column]

def d_p_q(p,q):
	top_fraction = p*q
	bottom_fraction = 1/(1-(p*(1-q) + (1-p)*q))
	return top_fraction*bottom_fraction
