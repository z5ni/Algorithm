S = input()
lst = []

for i in range(len(S)):
	lst.append(S[-i:])

lst.sort()
for l in lst:
	print(l)