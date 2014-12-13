s1 = list()
s2 = list()


def push():
	if((len(s1)+len(s2)) == num):
		print "overflow"
		sys.exit(0)
	print "enter the element"
	n = int(input("num:"))
	if(len(s2) == 0):
		s1.append(n)
	else:
		s2.append(n)
	print s1
	print s2

def pop():
	if((len(s1)+len(s2)) == 0):
		print "underflow"
		sys.exit(0)
	if(len(s2) == 0):
		while(len(s1) != 1):
			s2.append(s1[0])
			s1.remove(s1[0])
		print s1[0]
		s1.remove(s1[0])
	else:
		while(len(s2) != 1):
			s1.append(s2[0])
			s2.remove(s2[0])
		print s2[0]
		s2.remove(s2[0])


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
