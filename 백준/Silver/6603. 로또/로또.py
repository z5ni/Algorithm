def combi(n):
	if len(lotto) == 6:
		print(' '.join(map(str, lotto)))
		return

	for i in range(n, len(lst)):
		lotto.append(lst[i])	# 숫자 추가
		combi(i+1)	# 다음 숫자 선택
		lotto.pop()	# 방금 추가한 숫자 제거 후 다른 숫자로 시도


while True:
	N = input()
	if N == "0":
		break
	
	a = list(map(int, N.split()))
	R = a[0]
	lst = a[1:]
	lotto = []

	combi(0)
	print()
