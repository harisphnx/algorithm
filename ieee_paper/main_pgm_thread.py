
###################### Imports ##########################

from random import randint
from ete2 import Tree
from collections import deque
import threading


def allot_freq( units ):
	global balan_exe_time1
	if( (float(units)/400.0) > balan_exe_time1 ):
		if( (float(units)/533.0) > balan_exe_time1 ):
			return 800.0
		else:
			return 533.0
	elif( (float(units)/320.0) < balan_exe_time1 ):
		if( (float(units)/266.0) < balan_exe_time1 ):
			return 266.0
		else:
			return 320.0
	else:
		return 400.0
	

######################## Quicksort functions #######################

##### main quicksort function #####
 
def quicksort( aList, first, last, flag1, flag2 ):
	global a,b,c,d
	global a_units, b_units, c_units, d_units
	if(first < last):
		pivot = partition( aList, first, last )
		if( flag1 == 0 and flag2 == 1):
			### core 1 ###
			quicksort( aList, first, pivot - 1, 1, 0)  ### gave to core 2 ###
			quicksort( aList, pivot + 1, last, 1, 1)   ### in core 1 only ###
		if( flag1 == 1 and flag2 == 0):
			### core 2 ###
			c_units = (pivot - 1) - first
			print "core 3 units",c_units
			c = allot_freq( c_units )
			print "core 3 freq",c
			c = ( c_units ) / c
			b_units = last - (pivot + 1)
			print "core 2 units",b_units
			b = allot_freq( b_units )
			print "core 2 freq",b
			b = ( b_units ) / b
			core3_thread = threading.Thread(target = quicksort,args=(aList, first, pivot - 1, 0, 0))
			core3_thread.start()
			core2_thread = threading.Thread(target = quicksort,args=( aList, pivot + 1, last, 0, 0))
                        core2_thread.start()
			#quicksort( aList, first, pivot - 1, 0, 0)  ### gave to core 3 ###
                        #quicksort( aList, pivot + 1, last, 0, 0)   ### in core 2 only ###
		if( flag1 == 1 and flag2 == 1):
			### core 1 ###
			d_units = (pivot - 1) - first
			print "core 4 units",d_units
			d = allot_freq( d_units )
			print "core 4 freq",d
			d = ( d_units ) / d
			a_units = last - (pivot + 1) 
			print "core 1 units",a_units
			a = allot_freq( a_units )
			print "core 1 freq",a
			a = ( a_units ) / a
			core4_thread = threading.Thread(target = quicksort,args=(aList, first, pivot - 1, 0, 0))
                        core4_thread.start()
                        core1_thread = threading.Thread(target = quicksort,args=( aList, pivot + 1, last, 0, 0))
                        core1_thread.start()
			#quicksort( aList, first, pivot - 1, 0, 0)  ### gave to core 4 ###
                        #quicksort( aList, pivot + 1, last, 0, 0)   ### in core 1 only ###
		else:
			quicksort( aList, first, pivot - 1, 0, 0) 
                        quicksort( aList, pivot + 1, last, 0, 0)

##### partition function used to divide the array in two halves #####
 
def partition( aList, first, last ):
	pivot = randint( first, last - 1 )
	swap( aList, pivot, last )
	for i in range( first, last ):
		if( aList[i] <= aList[last] ):
			swap( aList, i, first )
			first += 1
	swap( aList, first, last )
	return first

##### swap function used to swap the two numbers #####

def swap( A, x, y ):
	tmp = A[x]
	A[x] = A[y]
	A[y] = tmp

###############################################################################


######################## Tree Traversal #############################

def addChild(node,n,level):
       	if level >= n or node.name == "":
               	return
        if( randint(0,4) ):
       	        node1 = node.add_child(name = randint(1, 10000))
               	addChild(node1,n,level+1)
        if( randint(0,4) ):
       	        node1 = node.add_child(name = randint(1, 10000))
               	level = level + 1
                addChild(node1,n,level)

def create_tree(t):
	root = randint(1, 10000)
	t.name = root
	n = 10
	node1 = t.add_child(name = randint(1, 10000))
	node2 = node1.add_child(name = randint(1, 10000))
	addChild(node2,n,2)
	node2 = node1.add_child(name = randint(1, 10000))
	addChild(node2,n,2)
	node1 = t.add_child(name = randint(1, 10000))
	node2 = node1.add_child(name = randint(1, 10000))
        addChild(node2,n,2)
        node2 = node1.add_child(name = randint(1, 10000))
        addChild(node2,n,2)
	return  len( t.get_descendants() )

def traverse(t, flag1, flag2):
	p= t.get_children()
	global a,b,c,d
	global c_units, b_units, d_units, a_units
	if( flag1 == 0 and flag2 == 1):
		### core 1 ###
                traverse( p[0], 1, 0)   ### gave to core 2 ###
                traverse( p[1], 1, 1)   ### in core 1 only ###
	if( flag1 == 1 and flag2 == 0):
        	### core 2 ###
		c_units = len( p[0].get_descendants() )
	        print "core 3 units",c_units
		c = allot_freq( c_units )
		print "core 3 freq",c
		c = float( c_units ) / c
		b_units = len( p[1].get_descendants() )
        	print "core 2 units",b_units
		b = allot_freq( b_units )
		print "core 2 freq",b
		b = float( b_units ) / b
		core3_thread = threading.Thread(target = traverse,args=( p[0], 0, 0))
		core3_thread.start()
		core2_thread = threading.Thread(target = traverse,args=( p[1], 0, 0))
		core2_thread.start()
	        #traverse( p[0], 0, 0)  ### gave to core 3 ###
        	#traverse( p[1], 0, 0)   ### in core 2 only ###
        if( flag1 == 1 and flag2 == 1):
	        ### core 1 ###
		d_units = len( p[0].get_descendants() )
        	print "core 4 units",d_units
		d = allot_freq( d_units )
		print "core 4 freq",d
		d = float( d_units / d )
		a_units = len( p[1].get_descendants() )
	        print "core 1 units",a_units
		a = allot_freq( a_units )
		print "core 1 freq",a
		a = float( a_units ) / a
		core4_thread = threading.Thread(target = traverse,args=( p[0], 0, 0))
                core4_thread.start()
                core1_thread = threading.Thread(target = traverse,args=( p[1], 0, 0))
                core1_thread.start()
        	#traverse( p[0], 0, 0)  ### gave to core 4 ###
	        #traverse( p[1], 0, 0)   ### in core 1 only ###


###############################################################################


########################### Finding Primes ##################################

##### main prime function (selects one element and checks for prime) #####

def finding_primes( aList ):
	core1 = len(aList)/4
	core2 = len(aList)/4
	core3 = len(aList)/4
	core4 = len(aList)/4
	a = allot_freq(core1)
	b = allot_freq(core2)
	c = allot_freq(core3)
	d = allot_freq(core4)
	print "core1 freq",a
	print "core2 freq",b
	print "core3 freq",c
	print "core4 freq",d
	
	print "core 1",core1
	print "core 2",core2
	print "core 3",core3
	print "core 4",core4
	for x in aList:
		prime(x) 

##### checks for prime #####

def prime(num):
	y = 0
	if num > 1:
  		# check for factors
		for y in range(2,num):
			if (num % y) == 0:
#		        	print num,"is not a prime number"
		        	break
		if( y == (num-1) ):
			print num,"is a prime number"
	# if input number is less than
	# or equal to 1, it is not prime
#	else:
#	   	print num,"is not a prime number"



###############################################################################

############################ N-Queens ##################################

chosen = {}

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

def NQueens(xpos, n):
        # print 'NQueens(',xpos,') entering'
        global Q_flag
        for ypos in range(1, n + 1):
                clear_all_future_positions(xpos)
                if place(xpos, ypos):
                        chosen[xpos] = ypos
                        # print 'chosen=',chosen
                        if (xpos==n):
                                for opponent in chosen:
                                        print chosen[opponent]
                                print '------------------'
                                Q_flag = 1
                        else:
                                if( Q_flag == 0 ):
                                        NQueens(xpos+1, n)
        # print 'NQueens(',xpos,') returns'




###############################################################################

########################### Main Program ################################
balan_exe_time1 = 0.0
a = b = c = d = 0.0
a_units = b_units = c_units = d_units = 0.0

flag = 1
while(flag == 1):
	print "enter the choice of the example you want to run\n"
	print "1: Quicksort\n2: Tree traversal\n3: Primes\n4: N-Queens\n"
	choice = int(raw_input(""))

	flag = 0

##### choose the type you want to check for DVFS #####

	if( choice == 1):
		### quicksort ###
		aList = []
		balan_exe_time1 = 10000.0/(4.0*800.0)
		for i in range(10000):
			aList.append( randint(1, 10000) )
		quicksort( aList, 0, len( aList ) - 1, 0, 1 )
		print aList
		print "normal execution time without DVFS", float( max(a_units, b_units, c_units, d_units) ) / 400.0 
		print "execution time with DVFS", float( max(a,b,c,d) )
		flag = int(raw_input("Continue?\n"))

	elif(choice == 2):
		### tree traversal ###

		t = Tree()
		balan_exe_time1 = float( create_tree(t) )/ (4.0*800.0)
		print t.get_ascii(show_internal=True)
		traverse(t, 0, 1)
		print "units", a_units, b_units, c_units, d_units
		print "normal execution time without DVFS", float( max(a_units, b_units, c_units, d_units)) / 400.0 
		print "execution time with DVFS", max(a,b,c,d)

		flag = int(raw_input("Continue?\n"))

	elif(choice == 3):
		### finding primes ###
		aList = []
		balan_exe_time1 = 10000.0/(4.0*800.0)
		for i in range(10000):
			aList.append(i)
		finding_primes( aList )
		print "normal execution time without DVFS", 10000.0/(4.0*400.0)
		print "execution time with DVFS", 10000.0/(4.0*800.0)
		flag = int(raw_input("Continue?\n"))

	elif(choice == 4):
		### N-Queens ###
		n = int(raw_input("Enter the number od Queens\n"))
		print "\n\n"
		Q_flag = 0
		NQueens(1, n)
		flag = int(raw_input("Continue?\n"))

	else:
		print "invalid choice, please enter a valid one \n"
		flag = 1

##################################################################################	
