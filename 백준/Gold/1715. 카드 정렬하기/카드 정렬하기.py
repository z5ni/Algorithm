import sys
import heapq

input = sys.stdin.readline
N = int(input().rstrip())
cards = []

for _ in range(N):
	heapq.heappush(cards, int(input().rstrip()))

cnt = 0

while len(cards) >= 2:
	c = heapq.heappop(cards) + heapq.heappop(cards)
	cnt += c

	heapq.heappush(cards, c)

	if not cards:
		break

print(cnt)