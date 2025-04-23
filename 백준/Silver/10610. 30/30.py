import sys

input = sys.stdin.readline

N = int(input().rstrip())
L = list(map(int, list(str(N))))
if sum(L) % 3 == 0 and 0 in L:
	print(''.join(map(str, sorted(L, reverse=True))))
else:
	print(-1)