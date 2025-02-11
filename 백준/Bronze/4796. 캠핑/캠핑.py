num = 1
while True:
	try:
		L, P, V = map(int, input().split())
		if L == 0:
			break
		print(f"Case {num}:", V // P * L + min(L, V % P))
		num += 1
	except:
		break