N, K = map(int, input().split())
min_k = min(K, N-K)

denominator = 1
numerator = 1

for k in range(min_k):
	denominator *= (k + 1)
	numerator *= (N - k)

print((numerator // denominator) % 10007)

