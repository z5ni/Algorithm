import sys

input = sys.stdin.readline
r, c = map(int, input().rstrip().split())
W = []
W1 = []
W2 = []

for _ in range(r):
	w = input().rstrip()
	W.append(w)

for i in range(c):
	word = ''
	for w in W:
		word += w[i]

	A = word.split('#')
	for a in A:
		if len(a) >= 2:
			W1.append(a)

for w in W:
	B = w.split('#')
	for b in B:
		if len(b) >= 2:
			W2.append(b)

print(sorted(W1 + W2)[0])
