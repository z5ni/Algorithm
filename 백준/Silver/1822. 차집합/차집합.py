Na, Nb = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

C = sorted(list(A-B))
print(len(C))
if len(C):
	print(' '.join(map(str, C)))