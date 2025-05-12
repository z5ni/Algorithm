import sys
from math import sqrt

input = sys.stdin.readline
M, N = map(int, input().rstrip().split())

is_prime = [True] * (N + 1)
is_prime[1] = False

for i in range(2, int(sqrt(N)) + 1):
	if not is_prime[i]:
		continue
	for j in range(2 * i, N + 1, i):
		is_prime[j] = False

for i in range(M, N + 1):
	if is_prime[i]:
		print(i)