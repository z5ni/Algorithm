import sys

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def lcm(a, b):
	return a * b // gcd(a, b)

input = sys.stdin.readline
N = int(input().rstrip())
for _ in range(N):
	M, N, x, y = map(int, input().rstrip().split())
	
	year = x

	l = lcm(M, N)

	while year <= l:
		if (year - y) % N == 0:
			print(year)
			break
		year += M

	else:
		print(-1)