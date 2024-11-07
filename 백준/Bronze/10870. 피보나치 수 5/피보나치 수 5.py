N = int(input())
arr = [-1] * (N + 2)


def recurse(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		rec = recurse(n - 1) + recurse(n - 2)
		arr[n] = rec
		return rec

print(recurse(N))