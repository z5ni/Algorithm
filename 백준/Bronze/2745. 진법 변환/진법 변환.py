import sys

input = sys.stdin.readline
N, B = input().rstrip().split()

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dep = 0
result = 0
B = int(B)

for n in N[::-1]:
	n = digits.index(n)
	result += n * (B ** dep)
	dep += 1

print(result)