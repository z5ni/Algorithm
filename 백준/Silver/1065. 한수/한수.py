import sys
input = sys.stdin.readline

N = int(input().rstrip())
cnt = 0

for n in range(1, N+1):
	if n < 100:
		cnt += 1
	else:
		s = str(n)
		l = len(s)

		step = int(s[1]) - int(s[0])

		for i in range(2, l):
			if step != int(s[i]) - int(s[i-1]):
				break
			cnt += 1

print(cnt)