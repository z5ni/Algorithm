import sys

input = sys.stdin.readline

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def lcm(a, b):
	return (a * b) // gcd(a, b)

T = int(input().rstrip())
for _ in range(T):
	a, b = map(int, input().rstrip().split())
	print(lcm(a, b))
