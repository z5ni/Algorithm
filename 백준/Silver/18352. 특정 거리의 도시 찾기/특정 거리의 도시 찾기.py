from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())
city = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

# print(N, M, K, X)

for _ in range(M):
	a, b = map(int, input().rstrip().split())
	city[a].append(b)


q = deque()
q.append((X, 0))	# 깊이 같이 저장
visited[X] = True
depth = {}

while q:
	node, level = q.popleft()
	depth[node] = level
	
	for adj_node in city[node]:
		if visited[adj_node]:
			continue
		q.append((adj_node, level + 1))
		visited[adj_node] = True

	if level == K + 1:
		break

result = []

for k, v in depth.items():
	if v == K:
		result.append(k)

result.sort()
if result:
	for r in result:
		print(r)
else:
	print(-1)