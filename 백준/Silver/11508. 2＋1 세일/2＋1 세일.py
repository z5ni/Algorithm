N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)

total = 0
for i in range(0, N, 3):
    group = lst[i:i+3]
    if len(group) == 3:
        total += group[0] + group[1]
    else:
        total += sum(group)

print(total)