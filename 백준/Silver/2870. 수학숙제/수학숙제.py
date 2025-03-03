import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
	S = input().rstrip()
	num = ''
	for i in range(len(S)):
		if S[i].isdecimal():
			num += S[i]
			if i == len(S) - 1:
				lst.append(num)
		else:
			lst.append(num)
			num = ''

result = list(map(int, [l for l in lst if l != '']))
[print(r) for r in sorted(result)]