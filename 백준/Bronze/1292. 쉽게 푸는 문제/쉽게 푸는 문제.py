A, B = map(int, input().split())
lst = []
num = 1

while len(lst) < B:
	lst.extend([num] * num)
	num += 1

print(sum(lst[A-1:B]))
