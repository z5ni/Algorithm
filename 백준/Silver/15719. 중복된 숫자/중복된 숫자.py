import sys

N = int(sys.stdin.readline())
total = 0
num = 0

for c in sys.stdin.read():
	if c == ' ' or c == '\n':
		if num != 0:
			total += num
			num = 0
	else:
		num = num * 10 + int(c)

total += num

ex = N * (N - 1) // 2
print(total - ex)