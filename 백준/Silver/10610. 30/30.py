import sys

input = sys.stdin.readline
N = list(map(int, input().rstrip()))

if sum(N) % 3 == 0 and 0 in N:
	print(''.join(map(str, sorted(N, reverse=True))))
else:
	print(-1)