import sys


input = sys.stdin.readline
a, b = map(int, input().rstrip().split())

# N은 약수의 개수가 홀수 -> 제곱 수

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

total = b - a

def floor_sqrt(n):
    left, right = 0, n
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

B = floor_sqrt(b)
A = floor_sqrt(a)
cnt = B - A

if cnt == 0:
	print(0)
else:
	g = gcd(cnt, total)
	n = cnt // g
	d = total // g

	print(f"{n}/{d}")