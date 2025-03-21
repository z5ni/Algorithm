import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().rstrip().split())
adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N+1)

for _ in range(M):
	x, y = map(int, input().rstrip().split())
	adj_list[x].append(y)
	adj_list[y].append(x)

for adj_node in adj_list:
	adj_node.sort()


def dfs(node):
	global adj_list, visited

	if visited[node]:
		return
	visited[node] = True

	print(node, end=' ')

	for adj_node in adj_list[node]:
		dfs(adj_node)

dfs(V)
print()

q = deque()
q.append(V)

bfs_visited = [False] * (N+1)
bfs_visited[V] = True

while q:
	node = q.popleft()
	print(node, end=' ')

	for adj_node in adj_list[node]:
		if bfs_visited[adj_node]:
			continue
		q.append(adj_node)
		bfs_visited[adj_node] = True

# print(adj_list)
# print(visited)