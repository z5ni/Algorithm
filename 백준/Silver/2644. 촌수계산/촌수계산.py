import sys
input = sys.stdin.readline
n = int(input().rstrip())
x, y = map(int, input().rstrip().split())
m = int(input().rstrip())

adj_list = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for _ in range(m):
	a, b = map(int, input().rstrip().split())
	adj_list[a].append(b)
	adj_list[b].append(a)

cnt = -1

def dfs(node, depth):
	global cnt
	if visited[node]:
		return
	visited[node] = True
	
	if node == y:
		cnt = depth

	for adj_node in adj_list[node]:
		dfs(adj_node, depth+1)
		

dfs(x, 0)
print(cnt)