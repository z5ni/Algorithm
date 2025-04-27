import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
A = set(map(int, input().rstrip().split()))
B = set(map(int, input().rstrip().split()))

print(len(A - B | B - A))
