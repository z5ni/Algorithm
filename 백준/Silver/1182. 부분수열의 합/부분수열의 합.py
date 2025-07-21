import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
cnt = 0

for i in range(1, n+1):
	P = list(combinations(lst, i))
	for p in P:
		if sum(p) == s:
			cnt += 1

print(cnt)