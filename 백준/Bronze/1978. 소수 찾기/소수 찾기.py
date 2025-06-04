import sys
from math import sqrt

input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
cnt = 0

M = max(lst)
is_prime = [True] * (M + 1)
is_prime[1] = False

for i in range(2, int(sqrt(M)) + 1):
	if not is_prime[i]:
		continue
	for j in range(2 * i, M + 1, i):
		is_prime[j] = False

for l in lst:
	if is_prime[l]:
		cnt += 1

print(cnt)