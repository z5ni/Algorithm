import sys

input = sys.stdin.readline
S = list(input().rstrip())
pal = {}

for s in S:
	pal[s] = pal.get(s, 0) + 1

pal = sorted(pal.items(), key=lambda x: (x[0], -x[1]))

result = ''
odd_cnt = 0
odd_string = ''
is_pal = True

for k, v in pal:
	if v % 2 == 0:
		result += k * (v // 2)
	else:
		if not odd_cnt:
			odd_string = k
			result += k * (v // 2)
			odd_cnt += 1
		else:
			is_pal = False
			break

if is_pal:
	print(result + odd_string + result[::-1])
else:
	print("I'm Sorry Hansoo")
