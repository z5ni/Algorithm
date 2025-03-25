import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
q = deque()
result = []

for i in range(N):
	q.append(i+1)

while q:
	for _ in range(M-1):
		q.append(q.popleft())
	result.append(q.popleft())


print("<", end='')
for i in range(len(result) - 1):
	print(f"{result[i]},", end=' ')
print(f"{result[-1]}>")