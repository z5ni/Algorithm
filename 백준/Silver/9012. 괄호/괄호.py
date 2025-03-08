from collections import deque
import sys

input = sys.stdin.readline
T = int(input().rstrip())
for t in range(T):
	st = deque()
	answer = "YES"
	S = input()
	for s in S:
		if s == "(":
			st.append(s)
		if s == ")":
			if st:
				st.pop()
			else:
				answer = "NO"
				break
	if len(st) != 0:
		answer = "NO"
	print(answer)

