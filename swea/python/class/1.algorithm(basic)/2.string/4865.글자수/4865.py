import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스

for test_case in range(1, T+1):

    # 입력
    str1 = input() # 길이 N
    str2 = input() # 길이 M

    # 풀이
    max_count = max(str2.count(i) for i in str1)
    print(f'#{test_case}', max_count)
