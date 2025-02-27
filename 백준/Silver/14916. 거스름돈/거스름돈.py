def min_coins(n):
    # 1원 또는 3원은 거슬러 줄 수 없음
    if n == 1 or n == 3:
        return -1
    
    # 10원 미만은 직접 처리
    if n < 10:
        if n == 2: return 1
        if n == 4: return 2
        if n == 5: return 1
        if n == 6: return 3
        if n == 7: return 2
        if n == 8: return 4
        if n == 9: return 3
        return 0  # 거스름돈이 0이면 0개
    
    # 10원 이상의 경우 5원짜리 동전 최대 사용
    # 5원짜리 동전을 최대한 사용하고 남은 금액에 대해 2원짜리로 처리
    if n % 5 == 0:
        return n // 5  # 5원짜리 동전만으로 나눠짐
    elif n % 5 == 1:
        if n >= 6:  # 5원짜리 1개 + 2원짜리 2개
            return (n // 5) + 2
        else:
            return -1
    elif n % 5 == 2:
        if n >= 2:  # 2원짜리 1개
            return (n // 5) + 1
        else:
            return -1
    elif n % 5 == 3:
        if n >= 8:  # 5원짜리 1개 + 2원짜리 3개
            return (n // 5) + 3
        else:
            return -1
    elif n % 5 == 4:
        if n >= 9:  # 5원짜리 1개 + 2원짜리 4개
            return (n // 5) + 2
        else:
            return -1

# 입력 받기
n = int(input())
print(min_coins(n))
