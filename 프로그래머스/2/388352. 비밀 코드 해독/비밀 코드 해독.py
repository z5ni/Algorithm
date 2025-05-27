from itertools import combinations

def test(lst, Q, ans):
    cnt = 0
    for i in range(len(Q)):
        if len(set(Q[i]) & set(lst)) == ans[i]:
            cnt += 1
    
    if cnt == len(Q):
        return True



def solution(n, q, ans):
    result = 0
    C = list(combinations(range(1, n+1), 5))
    for c in C:
        if test(c, q, ans):
            result += 1
    return result