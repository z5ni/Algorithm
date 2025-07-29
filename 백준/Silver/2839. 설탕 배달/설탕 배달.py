import sys

input = sys.stdin.readline
n = int(input().rstrip())

# 5킬로그램 갯수 점점 줄여가면서 생각하기
for i in range(0, n // 5 + 1)[::-1]:
	cnt = -1
	r = n - (i * 5)

	if r % 3 == 0:
		cnt = i + r // 3
		break

print(cnt)