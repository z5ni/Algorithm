import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
jews = []
bags = []
result = 0

for _ in range(N):
	jews.append(tuple(map(int, input().rstrip().split())))

for _ in range(K):
	bags.append(int(input().rstrip()))

jews.sort()
bags.sort()
idx = 0

# 작은 가방에서 넣을 수 있는 최대 값 어치 보석 찾기로 접근하는게 맞는 듯
# 각각 가방마다 넣을 수 있는 보석 리스트를 찾은 다음 거기서 가장 값 어치가 큰 걸 찾기?
pack = []
for bag in bags:
	for i in range(idx, len(jews)):
		if bag >= jews[idx][0]:
			heapq.heappush(pack, -jews[idx][1])
			idx = i + 1
		else:
			break
	if pack:
		result -= heapq.heappop(pack)

print(result)