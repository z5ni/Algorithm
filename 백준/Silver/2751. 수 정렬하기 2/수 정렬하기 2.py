import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    lst.append(int(sys.stdin.readline()))
    
lst.sort()

for l in lst:
    print(l)