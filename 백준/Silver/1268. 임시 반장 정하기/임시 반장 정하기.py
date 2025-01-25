N = int(input())
dic = {}
check = {}
for i in range(N):
	check[i+1] = set()

for i in range(N):
	lst = list(map(int, input().split()))
	dic[i+1] = lst

for k1, v1 in dic.items():
	for k2, v2 in dic.items():
		for i in range(len(v1)):
			if v1[i] == v2[i] and k1 != k2:
				# print(k1, k2)
				if not k1 in check:
					check[k1] = {k2}
				else:
					check[k1].add(k2)

a = sorted(check.items(), key=lambda x: (-len(x[1]), x[0]))
print(a[0][0])