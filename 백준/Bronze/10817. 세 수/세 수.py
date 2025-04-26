import sys

input = sys.stdin.readline
L = list(map(int, input().rstrip().split()))

print(sorted(L)[1])
