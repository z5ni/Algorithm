import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
n = int(input().rstrip())
num = [1, 5, 10, 50]
result = set()

C = list(combinations_with_replacement(range(4), n))

for c in C:
	s = 0
	for i in c:
		s += num[i]
	result.add(s)

print(len(result))