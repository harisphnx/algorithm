n = int(raw_input("enter the size\n"))
mat = [[]for i in range(n)]
mat1 = [[]for i in range(n)]
mode = 1
flag = 0
x = 0
y = 0

print "enter the matrix"
for i in range(n):
	for j in range(n):
		temp = int(raw_input(""))
		mat[i].append(temp)
print mat

for i in range((n/2)):
	for j in range( (n - ((flag*2) + 1))):
		temp1 = mat[x][y]
		while(mode == 1):
			if( (y+1) < (n - flag) ):
				temp2 = mat[x][y+1]
				mat[x][y+1] = temp1
				temp1 = temp2
				y = y + 1
			else:
				mode = 2
		while(mode == 2):
			if( (x + 1) < (n - flag) ):
				temp2 = mat[x+1][y]
				mat[x+1][y] = temp1
				temp1 = temp2
				x = x + 1
			else:
				mode = 3
		while(mode == 3):
			if( (y-1) >= flag):
				temp2 = mat[x][y-1]
				mat[x][y-1] = temp1
				temp1 = temp2
				y = y - 1
			else:
				mode = 4
		while(mode == 4):
			if( (x-1) >= flag):
				temp2 = mat[x-1][y]
				mat[x-1][y] = temp1
				temp1 = temp2
				x = x - 1
			else:
				mode = 1
		x = flag
		y = flag
	flag = flag + 1
	x = flag
	y = flag
#print mat
for i in range(n):
        for j in range(n):
		if(mat[i][j] != -1):
			mat1[i].append(mat[i][j])
print mat1
