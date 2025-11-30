import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    # 입력 받기
    str1 = input() # 짧은 문자열
    str2 = input() # 긴 문자열

    N = len(str1) # 짧은 문자열
    M = len(str2) # 긴 문자열

    # 겹치는 문자열 찾기
    answer = 0

    for i in range(M-N+1) :

        count = 0
        for j in range(N) :
            if str2[i+j] != str1[j] :
                break
            else :
                count += 1

        if count == N :
            answer = 1

    print(f'#{test_case} {answer}')

