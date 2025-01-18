N = int(input())
lst = []

for _ in range(N):
	x, y = map(int, input().split())
	lst.append((x, y))

lst = sorted(lst)

for l in lst:
	print(' '.join(map(str, l)))