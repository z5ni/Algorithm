import sys
import heapq

prior_q = []
input = sys.stdin.readline
N = int(input().rstrip())

for _ in range(N):
	x = -int(input().rstrip())
	
	if x:
		heapq.heappush(prior_q, x)
		# print(prior_q)

	elif not x:
		if prior_q:
			a = heapq.heappop(prior_q)
			print(-a)
		else:
			print(0)
