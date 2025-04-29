import sys
import heapq

min_heap_q = []
input = sys.stdin.readline
N = int(input().rstrip())

for _ in range(N):
	x = int(input().rstrip())
	if x == 0:
		if min_heap_q:
			a = heapq.heappop(min_heap_q)
			print(a)
		else:
			print(0)
		continue
	
	heapq.heappush(min_heap_q, x)
