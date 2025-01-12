T = int(input())

for _ in range(T):
	N = int(input())
	lst = []
	is_ok = "YES"

	for _ in range(N):
		n = input()
		lst.append(n)

	# 접두어 관계 => 서로 인접
	lst.sort()

	for i in range(1, N):
		if lst[i].startswith(lst[i-1]):
			is_ok = "NO"
			break

	print(is_ok)