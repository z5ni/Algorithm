N = int(input())
ropes = sorted([int(input()) for _ in range(N)], reverse=True)
result = -1
# 현재 로프 * 현재까지의 로프 개수

for i in range(N):
	weight = ropes[i] * (i+1)
	result = max(result, weight)
print(result)