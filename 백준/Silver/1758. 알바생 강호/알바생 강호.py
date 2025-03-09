import sys

input = sys.stdin.readline
N = int(input().rstrip())
L = []
tips = 0

for _ in range(N):
	L.append(int(input().rstrip()))

L = sorted(L, reverse=True)

for i in range(len(L)):
	tip = max(L[i] - (i + 1 - 1), 0)
	tips += tip

print(tips)

