def solution(A, B):
    # 기약분수 만들기 ㅡ 최대공약수 구해서 약분하기
    # 최대공약수 구하기 ㅡ 유클리드 호제법
    a, b = A, B  # 원본은 또 사용하기 위해 값 복사
    while b:  # 나머지가 0이 되면 끝
        a, b = b, a % b  # 유클리드 호제법
    gcd = a  # 0이 아닌 다른 하나가 최대공약수

    # 약분하기 ㅡ A는 분자, B는 분모
    A, B = A / gcd, B / gcd

    # 유한소수 ㅡ 분모의 소인수가 2와 5만 존재(30 불가)
    # 소인수 구하기 ㅡ 숫자를 하나씩 올려가면서 나눠보기
    factor = 2
    factors = []
    while factor <= B:  # 약수는 아무리 커봤자 본인이다
        if B % factor == 0:  # 나누어떨어지는 경우, 약수이다
            factors.append(factor)  # 약수 리스트에 추가한 후
            while B % factor == 0:  # 더 이상 나눠떨어지지 않을때까지 나누기
                B //= factor
        factor += 1

    # 소인수 리스트에서 2와 5가 아닌게 있는지 확인
    for f in factors:
        if f != 2 and f != 5:  # 하나라도 아닌게 있으면 무한소수
            return 2
    else:
        return 1  # 다 둘러봤는데 아닌게 없으면 유한소수

