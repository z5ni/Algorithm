import sys
from itertools import combinations

input = sys.stdin.readline

while True:
	n = input().rstrip()
	if n == '0':
		break
	n = list(map(int, n.split()))

	k, lst = n[0], n[1:]
	lst.sort()
	L = list(combinations(lst, 6))
	for l in L:
		print(' '.join(map(str, l)))
	print()