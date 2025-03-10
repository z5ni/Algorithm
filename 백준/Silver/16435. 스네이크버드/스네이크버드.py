import sys

input = sys.stdin.readline
N, L = map(int, input().rstrip().split())
H = sorted(list(map(int, input().rstrip().split())))

for h in H:
	if L >= h:
		L += 1

print(L)