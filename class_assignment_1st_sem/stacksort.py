s1 = list()
s2 = list()

print "sorting using stack"

print "enter the number of elements"
num = int(input("number:"))
print num

print "enter the elements to be sorted"
for x in range(num):
	n = int(input(""))
	s1.append(n)

for y in range(num):
	l = s1.pop()
	for x in range(num - 1):
		m = s1.pop()
		if(l<m):
			s2.append(m)
		else:
			s2.append(l)
			l=m
	s2.append(l)
	l = s2.pop()
	for x in range(num - 1):
		m = s2.pop()
		if(m<l):
			s1.append(m)
		else:
			s1.append(l)
			l=m
	s1.append(l)
	
print s1
