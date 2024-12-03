from sys import stdin
input = stdin.readline

N = int(input())
lst = []
freq = {}

for _ in range(N):
   n = int(input())
   lst.append(n)
   freq[n] = freq.get(n, 0) + 1
   
lst.sort()
print(round(sum(lst)/N))
print(lst[N//2])
max_freq = max(freq.values())
fre = sorted([k for k, v in freq.items() if v == max_freq])
print(fre[1] if len(fre) > 1 else fre[0])
print(lst[-1] - lst[0])