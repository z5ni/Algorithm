import sys

input = sys.stdin.readline
N = int(input().rstrip())
ent = [input().rstrip() for _ in range(N)]
exit = [input().rstrip() for _ in range(N)]
result = [ent.index(exit[i]) for i in range(N)]

over = set()

for i in range(N):
	for j in range(i+1, N):
		if result[i] > result[j]:
			over.add(exit[i])
			break

print(len(over))