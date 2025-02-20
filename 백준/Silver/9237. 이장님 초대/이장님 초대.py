N = int(input())
trees = sorted(list(map(int, input().split())), reverse=True)
lst = []

for i in range(1, N+1):
	lst.append(i + trees[i-1])

print(max(lst)+1)
