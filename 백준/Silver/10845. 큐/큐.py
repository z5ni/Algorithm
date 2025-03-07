from collections import deque
import sys

input = sys.stdin.readline
N = int(input().rstrip())
q = deque()
for _ in range(N):
	command = input().rstrip().split()
	c = command[0]
	if c == "push":
		q.append(int(command[1]))
	if c == "front":
		print(q[0] if q else -1)
	if c == "back":
		print(q[-1] if q else -1)
	if c == "pop":
		print(q.popleft() if len(q) else -1)
	if c == "size":
		print(len(q))
	if c == "empty":
		print(0 if q else 1)
