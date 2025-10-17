# 1.

def solution(n):
    factor = []
    for i in range(1, n + 1):  # 1부터 n까지 돌면서
        if n % i == 0:
            factor.append(i)

    return factor

# 2. 리스트 컴프리헨션

def solution(n):
    return [i for i in range(1, n+1) if n % i == 0]

