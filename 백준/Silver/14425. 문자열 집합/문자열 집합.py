N, M = map(int, input().split())
S1 = set()
S2 = list()
cnt = 0

for _ in range(N):
	S1.add(input())

for _ in range(M):
	S2.append(input())


for s in S2:
	if s in S1:
		cnt += 1

print(cnt)