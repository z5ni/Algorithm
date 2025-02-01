U, N = map(int, input().split())
lst = []

for _ in range(N):
	S, P = map(str, input().split())
	lst.append((S, int(P)))

from collections import Counter

point_cnt = Counter(x[1] for x in lst)

min_cnt = min(point_cnt.values())
min_price = min(price for price in point_cnt if point_cnt[price] == min_cnt)

lst.sort(key=lambda x: x[1])

for s, p in lst:
	if p == min_price:
		print(s, p)
		break

