import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스 수

for test_case in range(1, T+1) :

    # 입력
    N = int(input()) # 행/열 수
    matrix = [list(map(int, input().split())) for _ in range(N)] # 행렬받기

    # 90도 회전 -> 2번하면 180도, 3번하면 270도
    matrix90 = [[0] * N for _ in range(N)] # 새 행렬 만들기
    for i in range(N) : # matrix 행 순회
        for j in range(N) : # matrix 열 순회
            matrix90[j][N-1-i] = matrix[i][j]

    matrix180 = [[0] * N for _ in range(N)] # 새 행렬 만들기
    for i in range(N) : # matrix 행 순회
        for j in range(N) : # matrix 열 순회
            matrix180[j][N-1-i] = matrix90[i][j]

    matrix270 = [[0] * N for _ in range(N)] # 새 행렬 만들기
    for i in range(N) : # matrix 행 순회
        for j in range(N) : # matrix 열 순회
            matrix270[j][N-1-i] = matrix180[i][j]

    # 출력
    print(f'#{test_case}')
    for i in range(N):  # 각 행 인덱스
        row1 = ''.join(map(str, matrix90[i]))
        row2 = ''.join(map(str, matrix180[i]))
        row3 = ''.join(map(str, matrix270[i]))
        print(row1, row2, row3)
