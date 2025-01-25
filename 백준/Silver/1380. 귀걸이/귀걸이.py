sinario = 0

while True:
	N = int(input())

	if N == 0:
		break

	dic = {}
	names = []
	sinario += 1
	
	for _ in range(N):
		name = input()
		names.append(name)

	for _ in range(2 * N - 1):
		a, b = map(str, input().split())
		dic[a] = dic.get(a, 0) + 1

	for k, v in dic.items():
		if v == 1:
			print(f"{sinario} {names[int(k)-1]}")

	