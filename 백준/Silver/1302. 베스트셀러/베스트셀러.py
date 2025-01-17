N = int(input())
dic = {}

for _ in range(N):
	book = input()
	if book in dic:
		dic[book] += 1
	else:
		dic[book] = 1


best = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(best[0][0])

