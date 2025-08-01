import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
R = sorted([tuple(map(int, input().rstrip().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))
rooms = []

for r in R:
	if rooms and rooms[0] <= r[0]:
		heapq.heappop(rooms)

	heapq.heappush(rooms, r[1])

print(len(rooms))