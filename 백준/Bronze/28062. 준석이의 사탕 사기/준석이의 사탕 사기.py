N = int(input())
lst = list(map(int, input().split()))
result = 0

ev = [l for l in lst if l % 2 == 0]
od = sorted([l for l in lst if l % 2 != 0], reverse=True)

result += sum(ev)
result += sum(od[:len(od) - (len(od) % 2)])
print(result)