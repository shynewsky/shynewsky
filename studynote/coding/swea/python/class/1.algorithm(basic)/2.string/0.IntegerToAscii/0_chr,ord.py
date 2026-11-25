import sys
sys.stdin = open('input.txt')

T = 1 # 테스트 케이스 수

for test_case in range(1, T+1):

    # 입력
    N = int(input()) # 정수로 받아야 한다

    # 함수 테스트
    print(chr(65))  # A ㅡ chr() 숫자에서 문자로
    print(ord('A')) # 65 ㅡ ord() 문자에서 숫자로

    # 숫자형을 문자형으로 바꾸기
    print(chr(N + 48)) # '5'
