import sys
from math import sqrt, ceil

input = sys.stdin.readline
n = int(input().rstrip())

left, right = 0, 2**63

while left < right:
	mid = (left + right) // 2
	if mid * mid >= n:
		right = mid
	else:
		left = mid + 1

print(left)