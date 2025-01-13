N, M = map(int, input().split())
lst = []
dic = {}

for i in range(N+M):
	lst.append(input())

for l in lst:
	if l not in dic:
		dic[l] = 1
	else:
		dic[l] += 1

result = [k for k, v in dic.items() if v == 2]

result = sorted(result)
print(len(result))
for r in result:
	print(r)

