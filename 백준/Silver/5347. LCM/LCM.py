import sys

input = sys.stdin.readline
t = int(input().rstrip())

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

for _ in range(t):
	a, b = map(int, input().rstrip().split())
	result = (a * b) // gcd(a, b)
	print(result)
