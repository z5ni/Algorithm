K = int(input())
lst = []

for _ in range(K):
	n = int(input())
	lst.append(n)

	if n == 0:
		lst.pop()
		lst.pop()

print(sum(lst))