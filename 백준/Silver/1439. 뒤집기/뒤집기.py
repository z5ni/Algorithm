import sys

input = sys.stdin.readline
S = input().rstrip()

A = S.split('0')
B = S.split('1')
A = [a for a in A if a.strip()]
B = [b for b in B if b.strip()]

print(min(len(A), len(B)))