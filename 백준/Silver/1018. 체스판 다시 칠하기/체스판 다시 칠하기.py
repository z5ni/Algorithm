import sys
from collections import deque

input = sys.stdin.readline
chess1 = [[] for _ in range(8)]
chess2 = [[] for _ in range(8)]

# W부터 시작
for i in range(8):
	for j in range(8):
		if i % 2 == 0:
			if j % 2 == 0:
				chess1[i].append('W')
			else:
				chess1[i].append('B')
		else:
			if j % 2 == 0:
				chess1[i].append('B')
			else:
				chess1[i].append('W')

# B부터 시작
for i in range(8):
	for j in range(8):
		if i % 2 == 0:
			if j % 2 == 0:
				chess2[i].append('B')
			else:
				chess2[i].append('W')
		else:
			if j % 2 == 0:
				chess2[i].append('W')
			else:
				chess2[i].append('B')


N, M = map(int, input().rstrip().split())
board = [input().rstrip() for _ in range(N)]

def get_min_cnt(nv, mv):
	cnt1 = 0
	cnt2 = 0

	for i in range(8):
		for j in range(8):
			if chess1[i][j] != board[nv+i][mv+j]:
				cnt1 += 1
			if chess2[i][j] != board[nv+i][mv+j]:
				cnt2 += 1
	return min(cnt1, cnt2)

# print(board)

best = N * M
for n in range(N):
	for m in range(M):
		# 8x8 만들기 가능한 최초 좌표
		if (n + 7 >= N) or (m + 7 >= M):
			continue
		best = min(best, get_min_cnt(n, m))

print(best)
