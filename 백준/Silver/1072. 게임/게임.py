import sys

input = sys.stdin.readline
X, Y = map(int, input().rstrip().split())
Z = (Y * 100) // X

if Z >= 99:
	print(-1)
	exit()

def binary_search():
	left = 0
	right = X

	while left < right:
		mid = (left + right) // 2

		if (Y + mid) * 100 // (X + mid) != Z:
			right = mid

		else:
			left = mid + 1

	mid = (left + right) // 2
	return mid

print(binary_search())

