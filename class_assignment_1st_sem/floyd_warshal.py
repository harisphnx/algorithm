print "****floyd warshal****"
print "______________________\n"
n = int(input("enter the number of vertices in the graph\n"))

s1 = [[] for i in range(n)]

temp = 0
print "enter the edge values\n\n"
for x in range(n):
	for y in range(n):
		temp = int(input(""))
		s1[x].append(temp)

print s1

print s1[0][2]
print s1[2][1]

for z in range(0, n):
	for x in range(0, n):
		for y in range(0, n):
			if(s1[x][y] > s1[x][z] + s1[z][y]):
				temp1 = s1[x][z]
				temp2 = s1[z][y]
				s1[x].pop(y)
				temp = temp1 + temp2
				s1[x].insert(y,temp)

print s1
