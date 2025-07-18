import sys

input = sys.stdin.readline
n = int(input().rstrip())
base = 666
cnt = 0

while True:
	if '666' in str(base):
		cnt += 1
	if n == cnt: break
	base += 1

print(base)