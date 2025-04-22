import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
	n = int(input().rstrip())
	sort = {}

	for __ in range(n):
		
		a, b = input().split()
		if b in sort:
			sort[b].append(a)
		else:
			sort[b] = [a]

	cnt = 1
	for s in sort:
		# 옷 입어도 되고 안 입어도 되고
		cnt *= (len(sort[s]) + 1)

	# 안 입은 경우 제외
	print(cnt-1)
