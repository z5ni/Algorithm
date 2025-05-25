import sys


# 분모: 최소공배수
input = sys.stdin.readline
N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
X = int(input().rstrip())
result = list()

# 서로소: a, b의 최대공약수가 1
def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

for a in A:
	if gcd(a, X) == 1:
		result.append(a)

print(sum(result) / len(result))