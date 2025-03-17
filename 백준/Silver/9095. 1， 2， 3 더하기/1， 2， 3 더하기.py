import sys

input = sys.stdin.readline
T = int(input().rstrip())
dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4

for n in range(4, 11):
	dp[n] = dp[n-3] + dp[n-2] + dp[n-1]

for _ in range(T):
	t = int(input().rstrip())
	print(dp[t])