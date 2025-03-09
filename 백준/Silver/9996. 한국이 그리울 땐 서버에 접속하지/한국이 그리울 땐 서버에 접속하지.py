import re

N = int(input())
st, end = input().split("*")
pattern = f"^{st}.*{end}$"

for _ in range(N):
	file = input()
	if re.findall(pattern, file):
		print("DA")
	else:
		print("NE")