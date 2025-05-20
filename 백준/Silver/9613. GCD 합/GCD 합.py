import sys
from itertools import combinations

input = sys.stdin.readline
T = int(input().rstrip())

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

for _ in range(T):
	sum_value = 0
	L = list(map(int, input().rstrip().split()))
	n = L[0]
	L = L[1:]

	lst = list(combinations(L, 2))

	for l in lst:
		sum_value += gcd(l[0], l[1])

	print(sum_value)