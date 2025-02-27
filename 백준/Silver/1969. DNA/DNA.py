N, M = map(int, input().split())
lst = [input() for _ in range(N)]
hamming = ''
cnt = 0

for i in range(M):
	dic = {}
	for l in lst:
		if dic.get(l[i], 0):
			dic[l[i]] += 1
		else:
			dic[l[i]] = 1
	hamming += sorted(dic.items(), key=lambda x: (-x[1], x[0]))[0][0]

for i in range(M):
	for l in lst:
		if l[i] != hamming[i]:
			cnt += 1

print(hamming)
print(cnt)