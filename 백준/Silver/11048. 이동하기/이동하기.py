import sys

input = sys.stdin.readline
dp = []
n, m = map(int, input().rstrip().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
miro = [[] * (m + 1) for _ in range(n + 1)]

miro[0] = [0] * (m + 1)
for i in range(1, n + 1):
	miro[i] = [0] + list(map(int, input().rstrip().split()))

for i in range(1, n + 1):
	for j in range(1, m + 1):
		dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + miro[i][j] 

print(dp[n][m])

