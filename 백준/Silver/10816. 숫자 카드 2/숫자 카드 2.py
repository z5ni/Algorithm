N = int(input())
num = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))
dic = {}

for n in num:
	dic[n] = dic.get(n, 0) + 1

for c in card:
	print(dic.get(c) or 0, end=" ")