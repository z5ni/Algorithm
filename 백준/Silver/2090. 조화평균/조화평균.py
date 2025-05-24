import sys


# 분모: 최소공배수
input = sys.stdin.readline
n = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def lcm(a, b):
	return abs(a * b) // gcd(a, b)

def multi_lcm(lst):
	result = lst[0]
	for l in lst[1:]:
		result = lcm(result, l)
	return result

de = multi_lcm(A)
nu = 0
for a in A:
	a = de // a
	nu += a

g = gcd(de, nu)


print(f"{de // g}/{nu // g}")