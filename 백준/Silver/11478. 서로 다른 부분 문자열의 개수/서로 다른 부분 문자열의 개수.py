import sys

S = sys.stdin.readline().strip()
result = set()

for i in range(len(S)+1):
	for j in range(1, len(S)+1):
		a = S[i:j]
		if a:
			result.add(a)

print(len(result))