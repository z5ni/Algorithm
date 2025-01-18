N = int(input())
medal = []

for _ in range(N):
	b, p, q, r = map(int, input().split())
	medal.append((b, p*q*r, p+q+r))

medal = sorted(medal, key=lambda x: (x[1], x[2], x[0]))
print(medal[0][0], medal[1][0], medal[2][0])