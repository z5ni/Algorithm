def canto(n):
	if n == 0:
		return "-"
	else:
		return canto(n-1) + ' ' * 3 ** (n-1) + canto(n-1)


while True:
	try:
		N = int(input())
		print(canto(N))
	except Exception as e:
		break