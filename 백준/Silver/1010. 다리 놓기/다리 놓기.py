T = int(input())

for t in range(T):
	N, M = map(int, input().split())

	def bridge(n, m):
		if n == 0:
			return 1
		return m * bridge(n-1, m-1) // n

	print(bridge(N, M))
