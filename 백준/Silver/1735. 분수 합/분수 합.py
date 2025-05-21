import sys
from itertools import combinations

input = sys.stdin.readline
a1, b1 = map(int, input().rstrip().split())
a2, b2 = map(int, input().rstrip().split())

# 최대 공약수 구하기
def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

a = a1 * b2 + a2 * b1
b = b1 * b2
c = gcd(a, b)
print(a // c, b // c)

