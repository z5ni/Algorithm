import sys
from collections import deque

input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
	N, M = map(int, input().rstrip().split())
	q = deque(map(int, input().rstrip().split()))

	cnt = 0
	while q:
		if q[0] < max(q):
			q.append(q.popleft())

		else:
			q.popleft()
			cnt += 1

			if M == 0:
				break

		if M > 0:
			M = M - 1
		else:
			M = len(q) - 1

	print(cnt)
