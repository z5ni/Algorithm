import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
q = deque()

for _ in range(n):
	c = input().rstrip().split()
	if c[0] == "push":
		q.append(c[1])
	if c[0] == "pop":
		print(q.popleft() if q else -1)
	if c[0] == "size":
		print(len(q))
	if c[0] == "empty":
		print(0 if q else 1)
	if c[0] == "front":
		print(q[0] if q else -1)
	if c[0] == "back":
		print(q[-1] if q else -1)