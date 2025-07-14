import sys
input = sys.stdin.readline

n = int(input().rstrip())
xy = sorted([tuple(map(int, input().rstrip().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))

[print(x[0], x[1]) for x in xy]