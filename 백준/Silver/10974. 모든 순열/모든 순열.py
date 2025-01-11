N = int(input())

lst = list(range(1, N+1))
check = [False] * N
choose = []

def per(level):
	if level == N:
		print(' '.join(map(str, choose)))
		return

	for i in range(0, N):
		if check[i] == True:
			continue
		choose.append(lst[i])
		check[i] = True

		per(level+1)

		check[i] = False
		choose.pop()


per(0)