import sys
from itertools import combinations

input = sys.stdin.readline
A, B = map(int, input().rstrip().split())

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

result =  (A * B) // gcd(A, B)
print(result)
