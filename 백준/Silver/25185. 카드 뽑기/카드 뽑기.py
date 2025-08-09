import sys
from collections import Counter

input = sys.stdin.readline
T = int(input().rstrip())

def test1(L):
    s = set(L)
    for x in s:
        if x+1 in s and x+2 in s:
            return True
    return False

def test2(L):
    cnt = Counter(L)
    return any(v >= 3 for v in cnt.values())

def pair_cnt(L):
    return sum(v // 2 for v in Counter(L).values())

def test3(M, P, S):
    return (pair_cnt(M) + pair_cnt(P) + pair_cnt(S)) >= 2

for _ in range(T):
	cards = input().rstrip().split()
	M = []
	P = []
	S = []
	for n, a in cards:
		if a == 'm':
			M.append(int(n))
		elif a == 'p':
			P.append(int(n))
		else:
			S.append(int(n))

	if test1(M) or test1(P) or test1(S):
		print(":)")
	elif test2(M) or test2(P) or test2(S):
		print(":)")
	elif test3(M, P, S):
		print(":)")
	else:
		print(":(")