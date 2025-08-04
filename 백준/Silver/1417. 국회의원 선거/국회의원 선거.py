import sys
import heapq

input = sys.stdin.readline
n = int(input().rstrip())
dasum = int(input().rstrip())
candi = [-int(input().rstrip()) for _ in range(n - 1)]
heapq.heapify(candi)
cnt = 0

while candi:
	c = heapq.heappop(candi)
	if dasum > -c:
		break
	heapq.heappush(candi, c + 1)
	dasum += 1
	cnt += 1

print(cnt)