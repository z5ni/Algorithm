import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))
start, end = 1, max(trees)

while start <= end:
	mid = (start + end) // 2
	sum_cut = 0

	for t in trees:
		if t > mid:
			sum_cut += t - mid

	if sum_cut >= M:
		start = mid + 1
	else:
		end = mid - 1

print(end)
