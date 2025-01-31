from math import sqrt

def next_prime(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    
    if is_prime(n):
        return n
        
    next_num = n + 1
    while not is_prime(next_num):
        next_num += 1
    return next_num

N = int(input())
lst = [int(input()) for _ in range(N)]

for num in lst:
    print(next_prime(num))