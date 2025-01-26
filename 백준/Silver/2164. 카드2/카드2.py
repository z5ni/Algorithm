from collections import deque

q = deque()
N = int(input())
for n in range(1, N+1):
	q.append(n)

for i in range(N-1):
	q.popleft()
	a = q.popleft()
	q.append(a)

print(q[0])