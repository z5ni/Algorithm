import sys
from itertools import combinations

input = sys.stdin.readline
t = int(input().rstrip())

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

for _ in range(t):
	m_gcd = -1
	L = list(combinations(list(map(int, input().rstrip().split())), 2))
	for l in L:
		gcd1 = gcd(l[0], l[1])
		if m_gcd < gcd1:
			m_gcd = gcd1

	print(m_gcd)
		