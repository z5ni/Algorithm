import sys
from math import sqrt

input = sys.stdin.readline
n = int(input().rstrip())
ring = list(map(int, input().rstrip().split()))

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def lcm(a, b):
	return a * b // (gcd(a, b))

for r in ring[1:]:
	l = lcm(r, ring[0])
	print(f"{l // r}/{l // ring[0]}")


