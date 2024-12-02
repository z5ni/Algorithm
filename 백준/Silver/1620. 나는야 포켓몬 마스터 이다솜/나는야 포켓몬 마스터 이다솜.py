import sys
input = sys.stdin.readline

N, A = map(int, input().split())
poke = {}
num_to_name = []

for i in range(N):
   name = input().rstrip()
   poke[name] = i+1
   num_to_name.append(name)

for _ in range(A):
   q = input().rstrip()
   if q.isdigit():
       print(num_to_name[int(q)-1])
   else:
       print(poke[q])