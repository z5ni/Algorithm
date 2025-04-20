import sys

input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
	S = list(input().rstrip().split())
	# print(S)
	result = []

	for s in S:
		result.append(s[::-1])
	print(' '.join(result))