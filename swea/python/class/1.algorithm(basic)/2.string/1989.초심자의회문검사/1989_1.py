import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스 수

for test_case in range(1, T+1) :

    # 입력 받기
    string = input().strip() # 문자열 받기
    N = len(string)

    # 회문 찾기
    for i in range(N//2) :
        if string[i] != string[N-1-i] :
            print(f'#{test_case} 0')
            break
    else :
        print(f'#{test_case} 1')

