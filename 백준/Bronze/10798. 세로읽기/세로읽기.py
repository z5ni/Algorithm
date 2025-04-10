import sys

input = sys.stdin.readline
max_length = 0
L = []

for _ in range(5):
	S = input().rstrip()
	if len(S) > max_length:
		max_length = len(S)
	L.append(S)


for i in range(max_length):
	for l in L:
		if i <= len(l) - 1:
			print(l[i], end='')