T = int(input())

for _ in range(T):
	money = int(input())
	
	reminder = [25, 10, 5, 1]

	for r in reminder:
		coin = money // r
		money %= r
		print(int(coin), end=' ')
	print()

