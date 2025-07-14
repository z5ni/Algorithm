import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input().rstrip())
per = list(permutations(range(1, n + 1), n))
[print(' '.join(map(str, p))) for p in per]