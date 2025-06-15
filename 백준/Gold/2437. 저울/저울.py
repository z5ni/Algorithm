import sys

input = sys.stdin.readline
n = int(input().rstrip())
L = sorted(list(map(int, input().rstrip().split())))
target = 0

for l in L:
	if l > target + 1:
		break
	target += l

print(target + 1)