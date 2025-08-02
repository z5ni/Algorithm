import sys
import heapq

input = sys.stdin.readline
N = int(input().rstrip())
X = []

for _ in range(N):
	x = int(input().rstrip())

	if x != 0:
		heapq.heappush(X, (abs(x), x))
	else:
		if X:
			a = heapq.heappop(X)
			print(a[1])

		else:
			print(0)