R, N = map(int, input().split())
lst = sorted(input().split())
pwd = []

# 모음의 개수 -> 1<=모음개수<=R-2
def secu(n):
	if len(pwd) == R:
		cnt = len(set(pwd) & set(['a', 'e', 'i', 'o', 'u']))
		if 1 <= cnt and cnt <= R-2:
			print(''.join(sorted(pwd)))
			return

	for i in range(n, len(lst)):
		pwd.append(lst[i])
		secu(i+1)
		pwd.pop()

secu(0)
