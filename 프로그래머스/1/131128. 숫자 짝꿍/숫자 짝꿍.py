def solution(X, Y):
    x = [0] * 10
    y = [0] * 10
    
    for i in X:
        x[int(i)] += 1
    for i in Y:
        y[int(i)] += 1
    
    result = []

    for i in range(10)[::-1]:
        result += str(i) * min(x[i], y[i])
    
    if not result:
        return "-1"
    
    if result[0] == "0":
        return "0"

    return ''.join(map(str, result))