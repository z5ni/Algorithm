N = int(input())
lst = list(map(int, input().split()))

lst.sort()
a = len(lst) // 2

if N % 2 == 0:
	print(lst[a-1])
else:
	print(lst[a])