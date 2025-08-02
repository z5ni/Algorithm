import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
cards = list(map(int, input().rstrip().split()))
heapq.heapify(cards)


for _ in range(m):
	c = heapq.heappop(cards)
	d = heapq.heappop(cards)

	heapq.heappush(cards, c + d)
	heapq.heappush(cards, c + d)

print(sum(cards))