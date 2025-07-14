import sys
from itertools import combinations

input = sys.stdin.readline
L, C = map(int, input().rstrip().split())
alpha = sorted(list(input().rstrip().split()))

def check(a):
	b = {'a', 'e', 'o', 'i', 'u'}
	if len(set(a) & b) < 1: return False
	if len(set(a) - b) < 2: return False
	return True

pwd = list(combinations(alpha, L))
[print(''.join(p)) for p in pwd if check(p)]