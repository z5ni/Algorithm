import sys
import math

input = sys.stdin.readline
N = list(map(int, list(input().rstrip())))
dic = dict()

for n in N:
	dic[n] = dic.get(n, 0) + 1

dic[6] = math.ceil((dic.get(6, 0) + dic.get(9, 0)) / 2)
if not dic.get(9, 0) == 0:
	del dic[9]

t = sorted(dic.items(), key=lambda x: (-x[1]))
print(t[0][1])
