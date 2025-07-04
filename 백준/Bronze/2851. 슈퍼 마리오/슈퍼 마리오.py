scores = [int(input()) for _ in range(10)]

total = 0
best_score = 0

for s in scores:
    total += s
    if abs(100 - total) < abs(100 - best_score):
        best_score = total

    elif abs(100 - total) == abs(100 - best_score):
        best_score = max(best_score, total)

print(best_score)