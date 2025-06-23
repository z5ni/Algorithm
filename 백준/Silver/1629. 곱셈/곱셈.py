import sys

input = sys.stdin.readline
a, b, c = map(int, input().rstrip().split())

def power(a, b, c):
	if b == 0:
		return 1
	half = power(a, b // 2, c)
	if b % 2 == 0:
		return (half * half) % c
	else:
		return (a * half * half) % c

print(power(a, b, c))