s1 = list()
s2 = list()

f1 = -1
r1 = -1
f2 = -1
r2 = -1

def enqueue(o, x, y):
	x = x + 1
	o.insert(x, y)

def dequeue(o, x):
	x = x + 1
	l = o[x]
	return l

def push():
	if(((f1-r1)+(f2-r2)) == num):
		print "overflow"
		sys.exit(0)
	n = int(input("enter the number:"))
	if((f2 == -1) and (r2 == -1)):
		enqueue(s1, f1, n)
	else:
		enqueue(s2, f2, n)

def pop():
	if(f1 == -1 and f2 == -1):
		print "undeflow"
		sys.exit(0)
	if(f2 == -1):
		while(f1 == (r1 + 1)):
			n = dequeue(s1, r1)
			enqueue(s2, f2, n)
		n = dequeue(s1, (r1 + 1))
		f1 = -1
		r1 = -1
		return n
	else:
		while(f2 == (r2 + 1)):
			n = dequeue(s2, r2)
			enqueue(s1, f1, n)
		n = dequeue(s2, (r2 + 1))
		f2 = -1
		r2 = -1
		return n
 

print "the size of the queue"
num = int(input("num:"))

print "choose your options"
flag = 1

while(flag!=0):
	print "push = 1"
	print "pop = 2"
	print "exit = 0"
	flag = int(input("enter option:"))
	if(flag==1):
		push()
	elif(flag==2):
		pop()
