import sys

input = sys.stdin.readline

N = int(input().rstrip())
X = []
Y = [[] for _ in range(N)]
cnt_x = 0
cnt_y = 0

for _ in range(N):
	X.append(input().rstrip())

for i in range(N):	
	for x in X:
		Y[i].append(x[i])

for x in X:
	a = x.split('X')
	for c in a:
		if len(c) >= 2:
			cnt_x += 1

for y in Y:
	b = ''.join(y).split('X')
	for c in b:
		if len(c) >= 2:
			cnt_y += 1

print(cnt_x, cnt_y)