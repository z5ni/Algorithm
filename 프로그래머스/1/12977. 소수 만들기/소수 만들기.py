from itertools import combinations
from math import sqrt

def get_di(n):
    s = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return s

def is_prime(n):
    return len(get_di(n)) == 0

def solution(nums):
    cnt = 0
    nums = list(combinations(nums, 3))
    result = []
    for n in nums:
        result.append(sum(n))
    
    for r in result:
        if is_prime(r):
            cnt += 1
    
    return cnt