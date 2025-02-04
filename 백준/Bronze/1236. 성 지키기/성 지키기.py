N, M = map(int, input().split())
width = []
height = [''] * M
w_cnt = 0
h_cnt = 0

for _ in range(N):
	w = input()
	width.append(w)

for w in width:
	for i in range(M):
		height[i] += w[i]


for w in width:
	if not 'X' in w:
		w_cnt += 1


for h in height:
	if not 'X' in h:
		h_cnt += 1

print(w_cnt if w_cnt > h_cnt else h_cnt)