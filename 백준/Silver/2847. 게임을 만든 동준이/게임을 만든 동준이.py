import sys

input = sys.stdin.readline
N = int(input().rstrip())
L = [int(input().rstrip()) for _ in range(N)][::-1]
cnt = 0

for i in range(1, N):
	if L[i] >= L[i-1]:
		cnt += L[i] - L[i-1] + 1
		L[i] = L[i-1] - 1

print(cnt)
