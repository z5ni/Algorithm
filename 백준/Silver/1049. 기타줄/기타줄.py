N, M = map(int, input().split())
A = list()
B = list()

for _ in range(M):
	a, b = map(int, input().split())
	A.append(a)
	B.append(b)

a = min(A)
b = min(B)

if a == 0 or b == 0:
	print(0)
# 전부 다 낱개로 사는게 쌀 경우
elif a > b * 6:
	print(b * N)
else:
	a_cnt = N // 6
	remain = N % 6
	
	# 낱개 * 개수랑 패키지 가격 비교
	if remain * b > a:
		a_cnt += 1
		b_cnt = 0
	else:
		b_cnt = remain
	print(a_cnt*a + b_cnt*b)