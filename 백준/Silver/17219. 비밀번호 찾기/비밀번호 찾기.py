import sys

input = sys.stdin.readline
result = dict()
N, M = map(int, input().rstrip().split())

for _ in range(N):
	adr, pwd = input().rstrip().split()
	result[adr] = pwd

for _ in range(M):
	adr = input().rstrip()
	print(result[adr])