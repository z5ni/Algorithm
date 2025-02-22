N, K = map(int, input().split())
coin = []
cnt = 0

# 문제 조건에서 동전은 i-1과 i는 항상 배수 관계 -> 배수 관계면 숫자가 큰 동전을 선택
for _ in range(N):
	c = int(input())
	coin.append(c)

coin.sort(reverse=True)

for c in coin:
	cnt += K // c
	K = K % c

print(cnt)