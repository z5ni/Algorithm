import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
books = list(map(int, input().rstrip().split()))

A = sorted([b for b in books if b > 0], reverse=True)
B = sorted([-b for b in books if b < 0], reverse=True)
C = sorted(A[::M]+B[::M], reverse=True)

print(sum(C[1::]) * 2 + C[0])