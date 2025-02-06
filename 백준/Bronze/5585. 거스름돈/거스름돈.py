N = 1000 - int(input())
cnt = 0

remainder = [500, 100, 50, 10, 5, 1]

for r in remainder:
	cnt += N // r
	N = N % r

print(cnt)