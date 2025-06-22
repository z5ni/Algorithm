import sys

input = sys.stdin.readline
S = input().rstrip()

print(sum(map(int, S.split(','))))