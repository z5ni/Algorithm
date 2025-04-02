import sys
from collections import deque

input = sys.stdin.readline

while True:
	S = input().rstrip()
	answer = 'yes' 

	if S == '.':
		break

	st = deque()

	for s in S:
		if s == '(':
			st.append(s)
		elif s == '[':
			st.append(s)
		elif s == ')':
			if not st:
				answer = 'no'
			elif st.pop() != '(':
				answer = 'no'
		elif s == ']':
			if not st:
				answer = 'no'
			elif st.pop() != '[':
				answer = 'no'

	if len(st):
		answer = 'no'
	print(answer)