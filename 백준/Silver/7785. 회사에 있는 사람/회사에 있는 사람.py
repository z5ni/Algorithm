import sys

input = sys.stdin.readline
n = int(input().rstrip())
com = {}
result = []

for _ in range(n):
	name, status = map(str, input().rstrip().split())
	com[name] = status

com = sorted(com.items(), reverse=True)

for name, status in com:
	if status == "enter":
		print(name)
