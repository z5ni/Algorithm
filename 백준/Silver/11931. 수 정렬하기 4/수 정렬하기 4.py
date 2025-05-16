import sys

input = sys.stdin.readline
N = int(input().rstrip())
L = [int(input().rstrip()) for _ in range(N)]
[print(i) for i in sorted(L, reverse=True)]