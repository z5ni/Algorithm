while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
        
    # B를 더 작은 수로 선택 (nCr = nC(n-r))
    B = min(B, A-B)
    
    # 분자, 분모 따로 계산
    numerator = 1  # 분자
    denominator = 1  # 분모
    
    # B번 반복
    for i in range(B):
        numerator *= (A - i)
        denominator *= (i + 1)
    
    print(numerator // denominator)