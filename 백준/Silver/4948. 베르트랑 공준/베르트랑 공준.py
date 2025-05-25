import sys
from math import sqrt

input = sys.stdin.readline
N = 123456 * 2
is_prime = [True] * (N + 1)
is_prime[1] = False

for i in range(2, int(sqrt(N)) + 1):
    if not is_prime[i]: 
    	continue
    for j in range(2 * i, N + 1, i):
        is_prime[j] = False


while True:
	n = int(input().strip())
	
	if n == 0:
		break

	a = is_prime[n + 1 : n * 2 + 1].count(True)
	print(a)
