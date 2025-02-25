S = input()
S = list(S.split('.'))
result = []
check = True

for s in S:
	a = len(s) // 4
	remi = len(s) % 4
	b = remi // 2
	result.append(4 * a * "A" + 2 * b * "B")
	if remi % 2 != 0:
		check = False

if check:
	print('.'.join(result))
else:
	print(-1)

