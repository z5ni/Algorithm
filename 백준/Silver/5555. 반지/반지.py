find_str = input()
N = int(input())
rings = [input() * 2 for i in range(N)]
cnt = 0

for r in rings:
	if find_str in r:
		cnt += 1

print(cnt)