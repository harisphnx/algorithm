#path = [][]
#distance = [][]
visted=[]
n= int(raw_input("Enter the number of nodes"))
count = 0
i=0
graph=[[0 for j in range(n)] for i in range(n)]
prev = [[str(j) for j in range(n)] for i in range(n)] 
with open('./input.txt') as f:
	graph = [[float(x) for x in line.split(',')] for line in f]
i=0
sourceNode = 5
while count != n-1:
	minVal = 0
	minNode =0
	for j in range(0, n):
		minK = j
		for k in range(0, n):
			if i!=j:
				if graph[i][j] != max(graph[i][j],graph[i][k]*graph[k][j]):
					minK = k
				#	prev[i].append(k)
				#	print graph[i][j],graph[i][k],graph[k][j],i,j,k
				graph[i][j] = max(graph[i][j],graph[i][k]*graph[k][j])
			#	graph[j][i] = max(graph[i][j],graph[i][k]*graph[k][j])
		if minK != j:
			prev[i][j]=prev[i][j]+prev[i][minK]
		if i!=j:
			if minVal < graph[i][j]:
				if j not in visted:
					minVal = graph[i][j]
					minNode = j
	i = minNode
	visted.append(i)
	print i
	count= count+1

print "shortest path from 1st node is"
for j in range(0, n):
	print graph[0][j],prev[0][j]

