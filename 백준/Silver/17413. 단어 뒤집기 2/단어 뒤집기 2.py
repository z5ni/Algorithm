import sys
from collections import deque

input = sys.stdin.readline
S = deque(input().rstrip())
result = ''
a = ''
reverse = True

while S:
	s = S.popleft()
	if s == '<':
		reverse = False

	if s == '>':
		reverse = True
		a = a + s
		result += a
		a = ''
		continue

	if reverse and s != ' ':
		a = s + a
	else:
		a = a + s

	if reverse and s == ' ':
		result += a
		a = ''

print(result + a)