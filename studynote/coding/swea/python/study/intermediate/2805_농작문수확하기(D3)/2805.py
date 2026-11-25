T = int(input()) # 테스트케이스 수

for test_case in range(1, T+1):

    # 입력
    N = int(input()) # N*N 농장
    matrix = [list(map(int, input().strip())) for _ in range(N)]

    # 풀이
    sell = 0
    for i in range(N): # 행 순회
        for j in range(N): # 열 순회

            con1 = i + j > N//2 - 1
            con2 = i + j < N + N//2
            con3 = j <= i + N//2
            con4 = i <= j + N//2

            if con1 and con2 and con3 and con4:
                sell += matrix[i][j]

    print(f'#{test_case}', sell)
