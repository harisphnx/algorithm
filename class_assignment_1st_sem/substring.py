st = list()

def start(st, num, n):
	if (len(st)==0):
		print "string empty"
		sys.exit(0)
	elif(n>num):
		print "length of substr bigger than string"
		sys.exit(0)
	ans = list()
	for x in range(n):
		temp = st[x]
		ans.append(temp)
	print ans

def middle(st, num, n):
	if (len(st)==0):
		print "string empty"
		sys.exit(0)
	elif(n>num):
		print "length of substr bigger than string"
		sys.exit(0)
	ans = list()
	m = int(input("enter the starting index"))
	for x in range(n+1):
		if(x<m):
			continue
		temp = st[x]
		ans.append(temp)
	print ans

def end(st, num, n):
	if (len(st)==0):
		print "string empty"
		sys.exit(0)
	elif(n>num):
		print "length of substr bigger than string"
		sys.exit(0)
	ans = list()
	for x in range(num-1, num-n-1, -1):
		temp = st[x]
		ans.append(temp)
	ans.reverse()
	print ans


print "give the length of the string"
num = int(input(""))



print "enter the string"

for x in range(num):
	n = raw_input("")
	st.append(n)
print st


n = int(input("enter the range n:"))
print n

start(st, num, n)
middle(st, num, n)
end(st, num, n)




