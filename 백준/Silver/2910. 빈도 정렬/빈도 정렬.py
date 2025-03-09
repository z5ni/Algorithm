import sys

input = sys.stdin.readline
N, C = map(int, input().rstrip().split())
M = list(map(int, input().rstrip().split()))
M_d = dict()

for m in M:
	M_d[m] = M_d.get(m, 0) + 1

M_d2 = sorted(M_d.items(), key=lambda x: -x[1])

for k, v in M_d2:
	print(f"{str(k)} " * v, end="")