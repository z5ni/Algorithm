N, M = map(int, input().split())
def divide(n, m):
    if m == 0 or m == n:
        return 1
    return n * divide(n-1, m-1) // m

print(divide(N, M))