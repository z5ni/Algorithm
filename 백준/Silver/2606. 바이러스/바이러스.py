import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []

for _ in range(M):
	a, b = map(int, input().rstrip().split())
	adj_list[a].append(b)
	adj_list[b].append(a)


def dfs(node):

	if visited[node]:
		return
	visited[node] = True

	result.append(node)


	for adj_node in adj_list[node]:
		dfs(adj_node)

dfs(1)
print(len(result)-1)