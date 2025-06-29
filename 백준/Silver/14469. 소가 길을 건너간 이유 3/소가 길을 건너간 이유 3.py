import sys

input = sys.stdin.readline
n = int(input().rstrip())
cows = []

for _ in range(n):
	a, b = map(int, input().rstrip().split())
	cows.append((a, b))

cows = sorted(cows)
time = 0

for a, b in cows:
	if time < a:
		time = a
	time += b

print(time)