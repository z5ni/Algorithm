import sys

S = sys.stdin.readline()

def cycle(n):
	if 97 <= n <= 122:
		return chr(97 + (n - 97 + 13) % 26)
	elif 65 <= n <= 90:
		return chr(65 + (n - 65 + 13) % 26)
	else:
		return chr(n)

for s in S:
	print(cycle(ord(s)), end="")