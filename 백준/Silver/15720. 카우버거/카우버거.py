import sys

input = sys.stdin.readline
B, C, D = map(int, input().rstrip().split())
b = sorted(list(map(int, input().rstrip().split())), reverse=True)
c = sorted(list(map(int, input().rstrip().split())), reverse=True)
d = sorted(list(map(int, input().rstrip().split())), reverse=True)

dis = min(B, C, D)
print(sum(b) + sum(c) + sum(d))
disc = (sum(b[:dis]) + sum(c[:dis])+ sum(d[:dis]))*0.9
not_disc = sum(b[dis:])+sum(c[dis:])+sum(d[dis:])

print(int(disc+not_disc))