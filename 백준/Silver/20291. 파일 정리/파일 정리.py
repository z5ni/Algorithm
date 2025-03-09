import sys

input = sys.stdin.readline
N = int(input().rstrip())
ext = dict()

for _ in range(N):
	file = input().rstrip().split(".")[1]
	ext[file] = ext.get(file, 0) + 1

exts = sorted(ext.items(), key=lambda x: x[0])
for k, v in exts:
	print(k, v)