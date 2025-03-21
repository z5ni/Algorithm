import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
S = list(map(int, input().rstrip().split()))

dp = [min(S)] * N

dp[0] = S[0]
for i in range(1, N):
	dp[i] = max(dp[i-1], 0) + S[i]

print(max(dp))