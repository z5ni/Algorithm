import sys

input = sys.stdin.readline

X = int(input().rstrip())

# 몇 번째 줄인지 확인하기
N = 0

while X > N:
	X -= N
	N += 1


if N % 2 == 0:
	a = X
	b = N - X + 1
else:
	a = N - X + 1
	b = X

print(f"{a}/{b}")