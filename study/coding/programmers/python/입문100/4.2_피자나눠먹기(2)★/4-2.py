def solution(n):
    # 최대공약수 구하기
    a, b = 6, n
    while b:
        a, b = b, a % b
    gcd = a

    # 최소공배수 구하기
    lcm = (6 * n) // gcd
    return lcm // 6
