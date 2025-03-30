import sys
from collections import deque

input = sys.stdin.readline
hacking = dict()

N, M = map(int, input().rstrip().split())
hack = [[] for _ in range(N + 1)]
start = set()

for _ in range(M):
	A, B = map(int, input().rstrip().split())
	start.add(B)
	hack[B].append(A)

def bfs(node):
	visited = [False] * (N+1)
	q = deque()
	q.append(node)
	visited[node] = True
	cnt = 1

	while q:
		node = q.popleft()

		for b_node in hack[node]:
			if visited[b_node]:
				continue
			q.append(b_node)
			visited[b_node] = True
			cnt += 1

	return cnt

result = []
max_cnt = -1
for s in start:
	cnt = bfs(s)

	if cnt > max_cnt:
		max_cnt = cnt
		result = [s]

	elif cnt == max_cnt:
		result.append(s)

print(*sorted(result))