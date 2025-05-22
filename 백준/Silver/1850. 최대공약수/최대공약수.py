import sys
from itertools import combinations

input = sys.stdin.readline
a, b = map(int, input().rstrip().split())

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

print(gcd(a, b) * '1')