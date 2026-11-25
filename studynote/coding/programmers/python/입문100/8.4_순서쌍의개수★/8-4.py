# 1. for문

def solution(n):
    count = 0
    for a in range(1, n+1):
        if n % a == 0:  # a로 나누어 떨어질때
            b = n // a  # b는 몫이다 (나머지 없음)
            count += 1
    return count

# 2. while문

def solution(n):
    cnt = 0
    i = 1
    while i * i <= n:
        if n % i == 0:        # i가 약수면 (i, n//i) 한 쌍
            cnt += 2          # i와 n//i 두 개를 더함
            if i * i == n:    # n이 완전제곱이면 중복 하나 제거
                cnt -= 1
        i += 1
    return cnt

