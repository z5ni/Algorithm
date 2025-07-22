import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
L = list(permutations(A, N))
result = -1

for l in L:
	s = 0
	for i in range(1, N):
		s += abs(l[i] - l[i-1])
	result = max(result, s)

print(result)