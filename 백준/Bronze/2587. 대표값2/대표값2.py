import sys

input = sys.stdin.readline
L = sorted([int(input().rstrip()) for _ in range(5)])

print(sum(L)//len(L))
print(L[2])