import sys
from collections import deque

# input = sys.stdin.readline
S = input()
lst = []


for i in range(1, 13):
	lst.append('w' * i + 'o' * i + 'l' * i + 'f' * i)


for l in lst:
	S = S.replace(l, '1')


print(1 if S.isdigit() else 0)