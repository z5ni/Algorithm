import sys

input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
	x, y = map(str, input().rstrip().split())
	print("Distances: ", end='')
	for i in range(len(x)):
		a = ord(x[i])
		b = ord(y[i])

		print(b - a if b - a >= 0 else b - a + 26, end=' ')
	print()