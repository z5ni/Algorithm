import sys
from collections import deque

input = sys.stdin.readline

var = input().rstrip()

if var.startswith('_') or var.endswith('_') or "__" in var or var[0].isupper() or ('_' in var and any(c.isupper() for c in var)):
	print("Error!")

else:
	# C++
	if '_' in var:
		result = ''
		upp = False
		for v in var:
			if upp:
				result += v.upper()
				upp = False
			elif v == "_":
				upp = True
			else:
				result += v
	else:
		result = ''
		for v in var:
			if v.isupper():
				result += f"_{v.lower()}"
			else:
				result += v

	print(result)