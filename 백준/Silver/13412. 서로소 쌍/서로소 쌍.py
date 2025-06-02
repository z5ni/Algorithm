import sys
from math import sqrt

input = sys.stdin.readline
T = int(input().rstrip())


def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

for _ in range(T):
	n = int(input().rstrip())
	cnt = 0
	
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			a = i
			b = n // i

			if gcd(a, b) == 1:
				cnt += 1

	print(cnt)