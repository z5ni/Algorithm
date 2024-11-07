N = int(input())

def recurse(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return recurse(n -1) + recurse(n -2)

print(recurse(N))