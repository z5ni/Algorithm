cnt = 0

for i in range(8):
	n = input()
	if i % 2 == 0:
		cnt += n[::2].count('F')
	else:
		cnt += n[1::2].count('F')

print(cnt)