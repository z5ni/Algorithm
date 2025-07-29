import sys

input = sys.stdin.readline
S = int(input().rstrip())

for n in range(1, S + 1):
	if n * (n + 1) // 2 > S:
		print(n - 1)
		break
else:
	print(n)