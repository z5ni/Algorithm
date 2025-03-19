import sys

lst = [i for i in range(1, 10001)]
self_lst = []

def self_num(n):
	a = sum(list(map(int, (str(n)))))
	b = a + n
	self_lst.append(b)


for j in range(1, 10001):
	self_num(j)


for l in sorted(list(set(lst) - set(self_lst))):
	print(l)
