N = int(input())
lst = []

for _ in range(N):
	M = input()
	lst.append(M)

l = list(set(lst))
l.sort(key=lambda x: (len(x), x))

for a in l:
	print(a) 