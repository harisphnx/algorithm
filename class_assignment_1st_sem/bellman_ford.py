print "bellman-ford"

n = int(input("enter the number of vertices in thr graph\n"))

s = [[] for i in range(n)]

print "enter the edge weights"

for i in range(n):
	for j in range(n):
		temp = int(input(""))
		s[i].append(temp)

ans = [[] for i in range(2)]
ans[0].append(0)
ans[1].append(999)
for i in range(1, n):
	ans[0].append(999)
	ans[1].append(999)

print s
print ans

for i in range(0, n):
	if(ans[0][i] != 999):
		for j in range(0, n):
			for k in range(0, n):
				if(s[j][k] != 999 and s[j][k] != 100 and j != k):
					temp = s[j][k] + ans[0][j]
					if(temp < ans[0][k]):
						ans[0].pop(k)
						ans[0].insert(k,temp)
						ans[1].pop(k)
						ans[1].insert(k, j)

print ans
