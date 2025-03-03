result = set()

S = input()
result = set()
cnt = 0

for i in range(len(S)+1):
	for j in range(1, len(S)+1):
		a = S[i:j]
		if a:
			result.add(a)

print(len(result))