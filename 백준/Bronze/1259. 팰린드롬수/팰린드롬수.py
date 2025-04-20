import sys

input = sys.stdin.readline

while True:
	N = input().rstrip()
	result = "yes"

	if N == "0":
		break

	for i in range(len(N)):
		# print(N[i], N[len(N)-1-i])
		if not N[i] == N[len(N)-1-i]:
			result = "no"
			break 

	print(result)