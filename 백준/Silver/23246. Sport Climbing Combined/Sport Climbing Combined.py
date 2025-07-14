import sys
input = sys.stdin.readline
player = []

n = int(input().rstrip())
for _ in range(n):
	b, p, q, r = map(int, input().rstrip().split())
	player.append((b, p*q*r, p+q+r))

player = sorted(player, key=lambda x: (x[1], x[2], x[0]))
[print(player[i][0], end=' ') for i in range(3)]