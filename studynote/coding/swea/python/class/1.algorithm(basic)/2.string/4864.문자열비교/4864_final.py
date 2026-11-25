import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스

for test_case in range(1, T+1):

    # 입력
    str1 = input() # 길이 N
    str2 = input() # 길이 M

    # 풀이
    print(f'#{test_case}',1 if str1 in str2 else 0)
