def solution(numer1, denom1, numer2, denom2):
    # 통분해서 분수더하기
    numer3 = (numer1 * denom2) + (numer2 * denom1)
    denom3 = denom1 * denom2

    # 최대공약수 찾아서 약분하기
    a, b = numer3, denom3
    while b:  # 나머지가 0이 될때까지
        a, b = b, a % b  # 유클리드 호제법
    gcd = a  # 0이 아닌 다른 수가 최대공약수
    numer3, denom3 = numer3 // gcd, denom3 // gcd  # 약분하기

    return [numer3, denom3]  # 배열을 리턴하라고 했는데, 튜플로 리턴해도 문제가 안된다?
