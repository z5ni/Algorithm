result = set()

def func(S, start, end):
	return S[start:end]

S = input()
result = set()
cnt = 0

for i in range(len(S)+1):
	for j in range(1, len(S)+1):
		a = func(S, i, j)
		if a:
			result.add(a)

print(len(result))