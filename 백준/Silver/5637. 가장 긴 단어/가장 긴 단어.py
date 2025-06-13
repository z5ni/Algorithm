import sys
import re

input = sys.stdin.readline
word = ''

while True:
	S = input().rstrip()

	L = S.split()

	for s in L:
		s = re.sub(r'[^a-zA-Z-]', '', s)
		
		if len(s) > len(word):
			word = s

	if S:
		if S[-5:] == "E-N-D":
			break

print(word.lower())