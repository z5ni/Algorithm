import sys

input = sys.stdin.readline
t = int(input().rstrip())

for _ in range(t):
	m, n = map(str, input().rstrip().split())
	if m == "1":
		L = list(map(int, n.split('.')))[::-1]
		result = 0

		for i in range(8):
			result += 256 ** i * L[i]
		print(result)
	
	else:
		n = int(n)
		result = []
		for _ in range(8):
			result.append(n % 256)
			n = n // 256

		print('.'.join(map(str, result[::-1])))
