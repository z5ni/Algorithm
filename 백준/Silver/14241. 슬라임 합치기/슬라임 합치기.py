import sys
input = sys.stdin.readline

n = int(input().rstrip())
slime = list(map(int, input().rstrip().split()))
size = slime[0]
point = 0

for s in slime[1:]:
	point += size * s
	size += s

print(point)