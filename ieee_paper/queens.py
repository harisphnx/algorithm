
from math import *
import sys
 
chosen = {}
n = int(raw_input(""))
 
def place(xpos, ypos):
	if (ypos in chosen.values()):
		return False
	opponent = 1
	while(opponent < xpos):
		if abs(chosen[opponent]-ypos) == abs(opponent-xpos):
			return False
		opponent+=1
	return True
 
def clear_all_future_positions(xpos):
	for i in range(xpos,n+1):
		chosen[i]=None
 
def NQueens(xpos):
	# print 'NQueens(',xpos,') entering'
	global flag
	for ypos in range(1, n + 1):
		clear_all_future_positions(xpos)
		if place(xpos, ypos):
			chosen[xpos] = ypos
			# print 'chosen=',chosen
			if (xpos==n):
				for opponent in chosen:
					print chosen[opponent]
				print '------------------'
				flag = 1
			else:
				if( flag == 0 ):
					NQueens(xpos+1)
	# print 'NQueens(',xpos,') returns'
 
flag = 0 
NQueens(1) 
