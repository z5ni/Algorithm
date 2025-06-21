import sys

input = sys.stdin.readline
S = ''

while True:
	a = input().rstrip()
	S += a

	if a == '':
		break

print(sum(map(int, S.split(','))))