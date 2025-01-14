N = int(input())
lst = []

for i in range(N):
	lst.append(int(input()))

lst = sorted(lst)

for l in lst:
	print(l)