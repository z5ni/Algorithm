import sys

input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
	score = 0
	test = input().rstrip().split('X')

	for t in test:
		n = (len(t) * (len(t) + 1)) // 2
		score += n

	print(score)