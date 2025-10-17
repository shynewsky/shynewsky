# ** 0.5 : 제곱근 구하기
# int() 로 소숫점 버리고
# ** 2 : 다시 제곱헀을때 n 이면 제곱수

def solution(n):
    if int(n ** 0.5) ** 2 == n:
        return 1
    else:
        return 2
