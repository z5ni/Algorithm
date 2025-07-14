import sys
from itertools import combinations

input = sys.stdin.readline

while True:
	n = list(map(int, input().rstrip().split()))
	k, lst = n[0], n[1:]
	if k == 0:
		break

	lst.sort()
	L = list(combinations(lst, 6))
	for l in L:
		print(' '.join(map(str, l)))
	
	print()