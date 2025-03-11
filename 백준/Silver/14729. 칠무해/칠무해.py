import sys

input = sys.stdin.readline
n = int(input().rstrip())
L = []
for _ in range(n):
	L.append(float(input().rstrip()))

L.sort()
L = L[:7]

for l in L:
	print(f"{l:.3f}")