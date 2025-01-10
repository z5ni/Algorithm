L, C = map(int, input().split())
lst = sorted(list(input().split()))

choose = []

def combi(idx, level):
	if level == L:
		cnt = len(set(choose) & set(['a', 'e', 'i', 'o', 'u']))
		if cnt >= 1 and L-cnt >= 2 :
			print(''.join(choose))
		return

	for i in range(idx, len(lst)):
		choose.append(lst[i])
		combi(i+1, level+1)
		choose.pop()

combi(0, 0)
