import sys
sys.stdin = open('input.txt')

# str() 을 사용하지 않고 str()을 구현해라
# 5 를 '5' 로 만들기

""" 아스키코드
숫자 - 문자
48 - '0'
49 - '1'
50 - '2'
51 - '3'
52 - '4'
53 - '5'
54 - '6'
55 - '7'
56 - '8'
57 - '9'
"""

# 숫자를 한자리씩만 표현할 수 있기 때문에
# 한자리씩 떼서 48을 더하여 문자로 표현한다

T = 6

for test_case in range(1, T+1) :

    num = int(input())

    # 음수는 양수로 바꾼다
    isNegative = False
    if num < 0 :
        num *= -1
        isNegative = True

    # 일의자리부터 떼서
    # chr() 로 아스키코드의 숫자 문자로 바꾼뒤
    # result_str 에 누적하여 더한다
    string = ''
    while num > 0 :
        number = num % 10 # 일의자리 추출
        string = chr(number + 48) + string # 아스키 코드 문자로 바꿔 누적
        num //= 10 # 일의자리를 추출하고 남은 것으로 다음 반복 진행

    # 음수였을때 '-' 를 붙여 내보낸다
    if isNegative :
        string = '-' + string

    print(string)

