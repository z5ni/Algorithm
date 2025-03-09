import sys

input = sys.stdin.readline
N = int(input().rstrip())
L = set((map(int, input().rstrip().split())))
L = sorted(set(L))

for l in L:
	print(l, end=" ")