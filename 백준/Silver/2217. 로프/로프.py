N = int(input())
ropes = []

for _ in range(N):
    rope = int(input())
    ropes.append(rope)

ropes.sort(reverse=True)
max_weight = 0

for i in range(N):
    weight = ropes[i] * (i + 1)
    max_weight = max(max_weight, weight)

print(max_weight)