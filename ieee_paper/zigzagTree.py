from ete2 import Tree
from collections import deque
from random import randint

t = Tree()
def addChild(node,n,level):
	if level >= n or node.name == "":
		return
	
	if( randint(0,5) ):
		a = node.add_child(name = randint(1, 10000))
		addChild(a,n,level+1)
	if( randint(0,5) ):
		a = node.add_child(name = randint(1, 10000))
		level = level + 1
		addChild(a,n,level)





root = randint(1, 10000)
t.name = root
n = 10
a = t.add_child(name = randint(1, 10000))
addChild(a,n,2)
a = t.add_child(name = randint(1, 10000))
addChild(a,n,2)

print t.get_ascii(show_internal=True)
#print t.name,
#zigzag(deque(t.get_children()),0)
#print t.get_descendants()
p= t.get_children()
if( len(p) == 2):
	print "two"
	#print p[0]
	print len( p[0].get_descendants() )
	#print p[1]
	print len( p[1].get_descendants() )
else:
	print "one"
	#print p
	print len( p[0].get_descendants() )
	
