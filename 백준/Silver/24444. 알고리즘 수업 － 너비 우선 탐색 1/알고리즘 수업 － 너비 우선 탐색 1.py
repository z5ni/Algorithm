import sys
from collections import deque 
input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
lst = []
visit_order = [0] * (N + 1)
order = 1

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, N + 1):
	adj_list[i].sort()


q = deque()
q.append(R)
visited[R] = True
visit_order[R] = order
order += 1

while q:
	node = q.popleft()
	for adj_node in adj_list[node]:
		if visited[adj_node]:
			continue
		
		q.append(adj_node)
		visited[adj_node] = True
		visit_order[adj_node] = order
		order += 1

for i in range(1, N+1):
	print(visit_order[i])
