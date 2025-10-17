def solution(n):
    factors = []
    d = 2
    while d * d <= n:   # √n 까지만 검사
        if n % d == 0:
            factors.append(d)
            while n % d == 0:  # 중복 제거 위해 같은 소인수는 전부 나눠줌
                n //= d
        d += 1
    if n > 1:   # 마지막에 남은 소수가 있다면 추가
        factors.append(n)
    return factors
