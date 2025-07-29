import sys

input = sys.stdin.readline
n = int(input().rstrip())

for i in range(0, n // 5 + 1)[::-1]:
	cnt = -1
	r = n - (i * 5)

	if r % 3 == 0:
		cnt = i + r // 3
		break

print(cnt)