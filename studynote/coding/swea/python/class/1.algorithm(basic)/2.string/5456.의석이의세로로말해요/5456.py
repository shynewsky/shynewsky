T = int(input()) # 테스트 케이스

for test_case in range(1, T+1):

    # 입력
    N = 5
    matrix = [list(input()) for _ in range(N)]

    # 빈자리 채워넣기
    max_len = max([len(row) for row in matrix])
    for row in matrix :
        while len(row) != max_len :
            row += ['']

    # 전치행렬 만들기
    matrix = list(zip(*matrix))

    # 출력
    print(f'#{test_case}', ''.join([''.join(row) for row in matrix]))

