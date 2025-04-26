import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
keywords = set([input().rstrip() for _ in range(N)])

for _ in range(M):
	blog = set(input().rstrip().split(','))
	keywords -= blog

	print(len(keywords))