N = int(input())
s = set()

for _ in range(N):
	M = input()
	s.add(M)

lst = list(s)
lst.sort()
lst.sort(key=len)

for l in lst:
	print(l)
