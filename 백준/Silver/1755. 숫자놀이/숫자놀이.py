import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().rstrip().split())
dit = {
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
	"5": "five",
	"6": "six",
	"7": "seven",
	"8": "eight",
	"9": "nine",
	"0": "zero"
}
result = []
result_d = {}

for a in map(str, range(m, n+1)):
	c = ''
	for b in a:
		c = c + ' ' + dit[b]

	result.append(c)
	result_d[c] = a

cnt = 0
for r in sorted(result):
	if cnt == 10:
		cnt = 0
		print()
		print(result_d[r], end=' ')
		cnt += 1
	else:
		cnt += 1
		print(result_d[r], end=' '
			)