import sys

input = sys.stdin.readline
N = int(input().rstrip())
T = list(map(int, input().rstrip().split()))

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def lcm(a, b):
	return a * b // gcd(a, b)

result = T[0]
for i in range(1, len(T)):
	result = lcm(T[i], result)

print(result)