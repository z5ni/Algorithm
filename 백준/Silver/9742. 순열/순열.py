while True:
    try:
        lst, N = input().split()
        check = [False] * len(lst)
        per_list = []

        def per(level, choose):
        	if level == len(lst):
        		per_list.append(''.join(map(str, choose[:])))
        		return
        	
        	for i in range(0, len(lst)):
        		if check[i] == True:
        			continue
        		choose.append(lst[i])
        		check[i] = True

        		per(level + 1, choose)

        		check[i] = False
        		choose.pop()


        per(0, [])
        try:
        	string = per_list[int(N) - 1]
        	print(f"{lst} {N} = {string}")
        except:
        	print(f'{lst} {N} = No permutation')

    except EOFError:
        break