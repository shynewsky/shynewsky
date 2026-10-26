import sys
sys.stdin = open('input.txt')
INF = float('inf')

# 입력 ---------------------------------------
T = int(input()) # 수확횟수
for t in range(1, T+1):
    N = int(input()) # 당근개수 (3<=N<=1000)
    C = sorted(list(map(int, input().split()))) # 당근크기 (1<=Ci<=30)

    # 코드 ------------------------------------------------------

    # 1. 모든 경우의 수 만들기 -------------------------------------

    '''
    [1] [1] [1, 2, 3]
    [1] [1, 1] [2, 3]
    [1] [1, 1, 2] [3]
    [1, 1] [1] [2, 3]
    [1, 1] [1, 2] [3]
    [1, 1, 1] [2] [3]
    '''

    S = M = L = [] # 작은상자, 중간상자, 큰상자

    # for문으로 만들기
    # for i in range(1, N-1):
    #     for j in range(i+1, N):
    #         S = C[:i]
    #         M = C[i:j]
    #         L = C[j:]
    #         print(S, M, L)

    # while문으로 만들기
    # i = 1 # 1이상 N-2 미만
    # while i < N-1:
    #     j = i + 1  # i+1이상 N-1 미만
    #     while j < N:
    #         S = C[:i]
    #         M = C[i:j]
    #         L = C[j:]
    #         print(S, M, L)
    #         j += 1
    #     i += 1

    # 2. 같은 숫자는 같은 상자에 넣기 -----------------------------------------

    '''
    [1, 1, 1] [2] [3]
    '''

    min_len = INF

    # [첫번째 경계] 정하기 ---------------------------------------------------
    i = 1    # 1이상 N-2 미만
    while i < N-1:

        last_small = C[i-1] # 이전숫자
        if last_small != C[i]: # 이전숫자와 같지 않으면 구간자르기

            # [두번째 경계] 정하기 -------------------------------------------
            j = i + 1  # i+1이상 N-1 미만
            while j < N:

                last_medium = C[j-1] # 이전숫자
                if last_medium != C[j]: # 이전숫자와 같지 않으면 구간 자르기

                    # 자르기 -----------------------------------------------
                    # S = C[:i]
                    # M = C[i:j]
                    # L = C[j:]
                    # print(S, M, L)

                    lenS = i
                    lenM = j-i
                    lenL = N-j
                    # print(lenS, lenM, lenL)

                    # 3. 개수가 N//2 개 넘으면 불가능

                    if not (lenS > N//2 or lenM > N//2 or lenL > N//2):
                        len = max(abs(lenS-lenM), abs(lenM-lenL), abs(lenL-lenS))
                        # print(len)

                        # 4. 최대 개수 차이 중 최소

                        if min_len > len:
                            min_len = len

                j += 1
        i += 1

    print(f'#{t}', min_len if min_len != INF else -1)