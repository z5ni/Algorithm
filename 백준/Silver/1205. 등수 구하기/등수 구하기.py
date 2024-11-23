N, point, P = map(int, input().split())
rank = list(map(int, input().split())) if N > 0 else []

rank.append(point)
rank.sort(reverse=True)

if rank.index(point) + rank.count(point) - 1 < P:
	print(rank.index(point) + 1)
else:
	print(-1)