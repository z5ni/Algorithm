from collections import deque

def solution(s):
    s = deque(s)
    d = deque()

    while s:
        if not s:
            break
        
        a = s.popleft()
        
        if a == '(':
            d.append('(')
        
        if a == ')':
            if d:
                d.popleft()
            else:
                return False
            
    if d:
        return False
    
    return True