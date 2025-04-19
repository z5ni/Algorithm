import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

stat = []
for _ in range(N):
	a, b = map(str, input().rstrip().split())	
	stat.append([a, int(b)])

stat = sorted(stat, key=lambda x: x[1])

for _ in range(M):
	point = int(input().rstrip())
	start = 0
	end = len(stat) - 1

	while start <= end:
		mid = (start + end) // 2
		if point > stat[mid][1]:
			start = mid + 1
		else:
			end = mid - 1

	print(stat[start][0])
