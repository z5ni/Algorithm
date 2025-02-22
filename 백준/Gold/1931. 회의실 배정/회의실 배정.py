N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst = sorted(lst, key=lambda x: (x[1], x[0]))
result = []
result.append(lst[0])

for start, end in lst[1:]:
	if start >= result[-1][1]:
		result.append((start, end))

print(len(result))
