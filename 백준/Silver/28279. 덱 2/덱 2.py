import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
dq = deque()

for _ in range(n):
	c = input().rstrip().split()
	cm = c[0]

	if cm == '1':
		dq.appendleft(c[1])
	if cm == '2':
		dq.append(c[1])
	if cm == '3':
		print(dq.popleft()) if dq else print(-1)
	if cm == '4':
		print(dq.pop()) if dq else print(-1)
	if cm == '5':
		print(len(dq))
	if cm == '6':
		print(0) if dq else print(1)
	if cm == '7':
		print(dq[0]) if dq else print(-1)
	if cm == '8':
		print(dq[-1]) if dq else print(-1)