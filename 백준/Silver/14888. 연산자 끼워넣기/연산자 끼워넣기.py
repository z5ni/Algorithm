import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
L = list(map(int, input().rstrip().split()))
oper = L[0] * ["+"] + L[1] * ["-"] + L[2] * ["*"] + L[3] * ["/"]
results = []
P = set(permutations(oper, len(oper)))

for op in P:
	first = A[0]

	for i in range(len(op)):
		if op[i] == '*':
			result = first * A[1:][i]
		elif op[i] == '+':
			result = first + A[1:][i]
		elif op[i] == '/':
			if first < 0:
				result = (abs(first) // A[1:][i]) * -1
			else:
				result = first // A[1:][i]
		elif op[i] == '-':
			result = first - A[1:][i]

		first = result

	results.append(result)

print(max(results))
print(min(results))