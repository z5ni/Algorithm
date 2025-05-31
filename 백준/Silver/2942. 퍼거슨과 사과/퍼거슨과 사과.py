import sys
from math import sqrt

input = sys.stdin.readline
R, G = map(int, input().rstrip().split())

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

g = gcd(R, G)

cd = set()
for i in range(1, int(sqrt(g)) + 1):
	if g % i == 0:
		cd.add(i)
		cd.add(g//i)


for c in cd:
	print(c, R // c, G // c)