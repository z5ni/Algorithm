from itertools import combinations
nan = [int(input()) for i in range(9)]
nan_sum = sum(nan)

combi = combinations(nan, 2)

for c in combi:
	if sum(c) == sum(nan) - 100:
		a, b = c[0], c[1]
		break

nan.sort()

nan.remove(a)
nan.remove(b)

for n in nan:
	print(n)