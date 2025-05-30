import sys

input = sys.stdin.readline
N = int(input().rstrip())
trees = sorted([int(input().rstrip()) for _ in range(N)])
term = []

for i in range(1, len(trees)):
	term.append(trees[i] - trees[i-1])

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

t_gcd = term[0]

for t in term[1:]:
	t_gcd = gcd(t, t_gcd)

tree_cnt = (trees[-1] - trees[0]) // t_gcd + 1

print(tree_cnt - N)