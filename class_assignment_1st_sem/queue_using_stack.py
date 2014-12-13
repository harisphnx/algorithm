s1 = list()
s2 = list()

def enqueue():
	if((len(s1)+len(s2))==num):
		print "overflow"
		sys.exit(0)
	print "enter the element"
	n = int(input("num:"))
	s1.append(n)

def dequeue():
	if((len(s2)==0) and (len(s1)==0)):
		print "underflow"
		sys.exit(0)
	if(len(s2)==0):
		while(len(s1)!=0):
			n = s1.pop()
			s2.append(n)
	n = s2.pop()
	print n

print "the size of the queue"
num = int(input("num:"))

print "choose your options"
flag = 1

while(flag!=0):
	print "enqueue = 1"
	print "dequeue = 2"
	print "exit = 0"
	flag = int(input("enter option:"))
	if(flag==1):
		enqueue()
	elif(flag==2):
		dequeue()

