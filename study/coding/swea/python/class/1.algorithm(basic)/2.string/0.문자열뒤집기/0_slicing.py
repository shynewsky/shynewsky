import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스 수

for test_case in range(1, T+1):

    # 입력
    arr = input()
    N = len(arr)

    # 문자열 뒤집기
    arr = arr[::-1]

    # 출력
    print(arr)
