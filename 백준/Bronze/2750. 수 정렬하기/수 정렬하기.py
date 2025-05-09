import sys

input = sys.stdin.readline
n = int(input().rstrip())
[print(l) for l in sorted([int(input().rstrip()) for _ in range(n)])]