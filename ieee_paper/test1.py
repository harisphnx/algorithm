from ete2 import Tree
from collections import deque
from random import randint

t = Tree()
def addChild(node,n,level):
	if level >= n or node.name == "":
		return
	a = node.add_child(name = randint(1, 10000))
	addChild(a,n,level+1)

	a = node.add_child(name = randint(1, 10000))
	level = level + 1
	addChild(a,n,level)

def zigzag(childList,level):
	if level >= n-1:
		return
	newList=[]
	while len(childList) > 0 :
		child = childList.pop()
		print child.name,
		children = child.get_children()
		if len(children) > 0:
			if level % 2 == 0:
				newList.append(children[1])
				newList.append(children[0])
			else:
				newList.append(children[0])
				newList.append(children[1])
	zigzag(deque(newList),level+1)
			
root = randint(1, 10000)
t.name = root
n = 100
addChild(t,n,1)

print t.get_ascii(show_internal=True)
print t.name,
zigzag(deque(t.get_children()),0)

