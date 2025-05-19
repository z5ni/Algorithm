import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split(':'))

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

gcd = gcd(n, m)
print(f"{n // gcd}:{m // gcd}")

