N = input()
if int(N) < 10:
	N = f"0{N}"

a = list(map(int, N))
cnt = 1

while True:
	if f"{a[-1]}{str(sum(a))[-1]}" == N:
		break
	else:
		a = list(map(int, f"{a[-1]}{str(sum(a))[-1]}"))
		cnt += 1

print(cnt)