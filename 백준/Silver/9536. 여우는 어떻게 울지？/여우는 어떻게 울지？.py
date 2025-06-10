import sys

input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
	a = input().strip().split()
	an = set()

	while True:
		S = input().strip()

		if S == "what does the fox say?":
			break

		S = S.split()
		an.add(S[-1])

	b = set(a) - an

	for c in a:
		if c in b:
			print(c, end=" ")