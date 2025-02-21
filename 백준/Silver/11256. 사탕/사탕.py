T = int(input())
for _ in range(T):
	J, N = map(int, input().split())
	lst = []

	for _ in range(N):
		r, c = map(int, input().split())
		lst.append(r * c)

	lst.sort(reverse=True)
	ls_sum = 0
	cnt = 0
	for i in range(len(lst)):
		ls_sum += lst[i]
		cnt += 1
		if ls_sum >= J:
			print(cnt)
			break
