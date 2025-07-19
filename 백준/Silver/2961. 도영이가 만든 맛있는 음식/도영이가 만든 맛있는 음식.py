import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input().rstrip())
L = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
result = 1000000000

for i in range(1, N+1):
	reci = list(combinations(L, i))

	for re in reci:
		s = 1
		ss = 0

		for j in range(len(re)):
			s = s * re[j][0]
			ss = ss + re[j][1]
		
		result = min(result, abs(s - ss))

print(result)