X = int(input())
cnt = 0

while True:
	if X < 10:
		print(cnt)
		if X % 3 == 0:
			print("YES")
		else:
			print("NO")
		break
	X = sum(list(map(int, list(str(X)))))
	cnt += 1