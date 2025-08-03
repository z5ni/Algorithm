import sys
import heapq

input = sys.stdin.readline
n = int(input().rstrip())
lec = []

for _ in range(n):
	p, d = map(int, input().rstrip().split())
	lec.append((d, p))

lec.sort()
pay = []

for d, p in lec:
	heapq.heappush(pay, p)
	
	# 마감일 지났으면 젤 작은 페이부터 pop
	if len(pay) > d:
		heapq.heappop(pay)

print(sum(pay))