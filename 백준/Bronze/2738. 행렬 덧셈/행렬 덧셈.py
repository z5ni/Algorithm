N, M = map(int, input().split())
a = list()
b = list()

for n in range(N):
	lst = list(map(int, input().split()))
	a += lst

for n in range(N):
	lst = list(map(int, input().split()))
	b += lst

c = [x + y for x, y in zip(a, b)]
result = [c[i:i + 3] for i in range(0, len(c), 3)]

for r in result:
	print(' '.join(map(str, r)))