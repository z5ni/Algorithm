N, new_point, P = map(int, input().split())
rank = list(map(int, input().split())) if N > 0 else []

new_rank = rank[:P]
new_rank.append(new_point)
new_rank.sort(reverse=True)

if new_rank.index(new_point) + new_rank.count(new_point) - 1 < P:
	print(new_rank.index(new_point) + 1)
else:
	print(-1)