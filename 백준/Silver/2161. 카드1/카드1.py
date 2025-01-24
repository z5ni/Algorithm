from collections import deque

N = int(input())
tr = []
q = deque()

for n in range(1, N+1):
	q.append(n)

for _ in range(N-1):
	a = q.popleft()
	tr.append(a)
	b = q.popleft()
	q.append(b)

tr.append(q[0])

print(' '.join(map(str, tr)))

