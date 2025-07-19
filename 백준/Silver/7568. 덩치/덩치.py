import sys
input = sys.stdin.readline
N = int(input().rstrip())
L = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

for i in range(N):
	rank = 1
	for j in range(N):
		if i == j:
			continue

		if L[j][0] > L[i][0] and L[j][1] > L[i][1]:
			rank += 1

	print(rank, end=' ')