queue1=list();
queue2=list();
mx=60
front1=front2=rear1=rear2=-1
print front1
print rear1


num=raw_input("enter number of elements:");
for i in range (int(num)):
	n=raw_input("num:")
	queue1.append(int(n))
	rear1=rear1+1
	front1=0;
print queue1

def push(a):
    global front1,rear1,front2,rear2
    if(rear1<mx and rear2<mx):
	if(front1==-1 and front2==-1):
		queue1.append(int(a));
		front1=0;
		rear1=rear1+1;
	elif(front1==-1 or front1>rear1):
		queue2.append(int(a))
		rear2=rear2+1;
	else:
		queue1.append(int(a))
		rear1=rear1+1
    else:
	print "overflow"
def popp():
	global front1,rear1,front2,rear2
	temp=0	
	temp2=0
	if(front1==front2==-1 or (front1>rear1 and front2>rear2)):
		print "underflow"
		sys.exit(0)
	elif(front1==-1 or front1>rear1):
		while not front2==rear2:
			temp=queue2[front2]
			queue2.pop([int(front2)])
			queue1.append(int(temp))
			front2=front2+1
			front1=0;
			rear1=rear1+1
		front2=front2+1
		front2=rear2=-1		
	elif(front2==-1 or front2>rear2):
		while not front1==rear1:
			temp=queue1[front1]
			queue1.pop([int(front1)])
			queue2.append(int(temp))
			front2=0
			rear2=rear2+1
			front1=front1+1
		front1=front1+1
		front1=rear1=-1	
	print front1
	print rear1
	print front2
	print rear2	
def decision():
	d=int(input("push(1) or pop(2)"))
	if(d==1):
    		a=int(input("enter the number to be pushed"))
    		push(a)
	elif(d==2):
		popp()

decision()
print queue1
print queue2

dec=int(input("more operations? yes(1) or no(2)"))
if(dec==1):
	decision()
	print queue1
	print queue2
else:
	pass

