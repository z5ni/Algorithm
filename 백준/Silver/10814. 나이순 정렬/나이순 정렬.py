N = int(input())
lst = []

for _ in range(N):
	a, b = input().split()
	lst.append([int(a), b])


C = sorted(lst, key=lambda x: x[0])

for c in C:
	print(c[0], c[1])