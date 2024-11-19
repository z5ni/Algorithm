N, K = map(int, input().split())
K = min(K, N-K)

n = 1
k = 1

for i in range(K):
	n *= (N-i)
	k *= (1+i)

print(n // k)