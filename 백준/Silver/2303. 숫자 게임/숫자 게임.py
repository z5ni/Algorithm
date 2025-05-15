import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input().rstrip())
di = {}

for i in range(N):
	C = map(int, input().rstrip().split())
	lar = -1
	T = list(combinations(C, 3))
	for t in T:
		if sum(t) % 10 > lar:
			lar = sum(t) % 10

	di[i + 1] = lar

di = sorted(di.items(), key=lambda x: (-x[1], -x[0]))
print(di[0][0])