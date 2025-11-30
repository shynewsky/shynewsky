T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    for i in range(N):  # 기준점 행 이동
        for j in range(N):  # 기준점 열 이동
            here = matrix[i][j]
            sum = 0  # 한번 내리칠때 잡는 파리 수

            for k in range(M) :
                for l in range(M) :

                    ni, nj = i+k, j+l

                    if 0<= ni <N and 0<= nj < N :
                        sum += matrix[ni][nj]

            if max_sum < sum :
                max_sum = sum

    print(f'#{test_case} {max_sum}')