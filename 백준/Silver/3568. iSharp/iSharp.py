import sys

input = sys.stdin.readline
var_list = input().strip().split(',')
var = var_list[0].split()[0]
var_list[0] = var_list[0].split()[1]

for v in var_list:
	b = ''
	c = ''
	for a in v:
		if a.isalpha():
			b += a
		elif a == ';':
			pass
		else:
			c = a + c
			
	c = c.replace('][', '[]')

	print(f"{var}{c.strip()} {b.strip()};")