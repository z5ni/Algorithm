import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
A = sorted(list(map(int, input().rstrip().split())))
print(A[K-1])