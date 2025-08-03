import sys
import heapq

input = sys.stdin.readline
n = int(input().rstrip())
lec = []
clas = []

for _ in range(n):
	_, s, e = map(int, input().rstrip().split())
	lec.append((s, e))

lec.sort()

for l in lec:
	if clas and clas[0] <= l[0]:
		heapq.heappop(clas) 

	heapq.heappush(clas, l[1])

print(len(clas))