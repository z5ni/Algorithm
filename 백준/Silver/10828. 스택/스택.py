from collections import deque
import sys

input = sys.stdin.readline
st = deque()
N = int(input())

for _ in range(N):
	c = input().split()
	if c[0] == "push":
		st.append(int(c[1]))
	if c[0] == "pop":
		print(st.pop() if st else -1)
	if c[0] == "size":
		print(len(st))
	if c[0] == "empty":
		print(0 if st else 1)
	if c[0] == "top":
		print(st[-1] if st else -1)