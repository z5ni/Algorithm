import sys

input = sys.stdin.readline
n = int(input().rstrip())
L1 = sorted([int(input().rstrip()) for _ in range(n)])
L2 = list(range(1, n + 1))
gap = 0

for i in range(n):
	g = L1[i] - L2[i]
	if g > 0:
		gap += g
	else:
		gap -= g

print(gap)
