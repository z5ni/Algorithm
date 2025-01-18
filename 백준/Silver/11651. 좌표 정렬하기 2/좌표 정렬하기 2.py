N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst = sorted(lst, key=lambda x: (x[1], x[0]))
for x, y in lst:
	print(x, y)