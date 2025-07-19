import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input().rstrip())
L = [list(map(int, input().rstrip().split())) for _ in range(N)]
synergy = dict()

couple = list(combinations(range(N), 2))

for c in couple:
	synergy[c] = L[c[0]][c[1]] + L[c[1]][c[0]]

teams = list(combinations(range(N), N // 2))
match = set()
point = 100 * N

for team in teams:
	start = set(team)
	link = set(range(N)) - start

	s_point = 0
	l_point = 0

	S = list(combinations(start, 2))
	L = list(combinations(link, 2))

	for i in range(len(S)):
		s_point += synergy[S[i]]
		l_point += synergy[L[i]]

	point = min(point, abs(s_point - l_point))

print(point)