import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    # 입력
    A, B = input().split()
    N, M = len(A), len(B)

    # str2가 str1에 있는 것을 확인하면
    # 인덱스를 뛰어넘고 다시 탐색한다

    idx = 0
    count = 0

    while idx < N:
        count += 1
        if A[idx:idx+M] == B :
            idx += M
        else :
            idx += 1

    print(f'#{test_case}', count)
