import sys
import heapq

input = sys.stdin.readline
n = int(input().rstrip())
lec = []
clas = []

for _ in range(n):
	_, s, e = map(int, input().rstrip().split())
	lec.append((s, e))

heapq.heapify(lec)

while lec:
	a = heapq.heappop(lec)

	if clas and clas[0] <= a[0]:
		heapq.heappop(clas) 

	heapq.heappush(clas, a[1])

print(len(clas))