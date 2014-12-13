arr = [[] for i in range(5)]
for i in range(5):
	for j in range(5):
		arr[i].append(0)
print arr
count = 0
n = 5
lights = 0

for i in range(0, (n-2)):
	for j in range(0, (n-2)):
		for x in range(i, (i+3)):
			for y in range(j, (j+3)):
				count = count + arr[x][y]
		if(count < 4):
			print "in1"
			print count
			temp1 = 4 - count
			if(i > j or i == j):
				for x in range(i,(i+3)):
					if(arr[x][j+2] == 0 and temp1 > 0):
						print "in21"
						arr[x][j+2] = 1
						lights = lights + 1
						temp1 = temp1 - 1
				if(temp1 > 0):
					print "in22"
					arr[x][j] = 1
					lights = lights + 1
					temp1 = temp1 - 1
			else:
				for x in range(j,(j+3)):
					if(arr[i+2][x] == 0 and temp1 > 0):
						print "in31"
						arr[i+2][x] = 1
						lights = lights + 1
						temp1 = temp1 - 1
				if(temp1 > 0):
					print "in32"
					arr[i+2][x] = 1
					lights = lights + 1
					temp1 = temp1 - 1
		print arr
		count = 0


print arr
print lights

