T = int(input())
for test_case in range(1, T + 1):

    # 방1) 델타

        # 기준점(i,j)을 중심으로
        # 오른쪽으로 M행 M열 의 파리 합 중
        # 한번 내리쳐서 최대한 많이 죽일 수 있는 파리 수

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

    # 방2) 리스트슬라이싱 (ㄱㅅㄱ님)

    max_sum = -1
    row_, col_, r_, l_ = 0, 0, 0, 0
    for i in range(100):
    
        for j in range(100):
            row_ += delta[i][j]    # 행 값 누적
            col_ += delta[j][i]    # 열 값 누적
            if i == j:             # 대각선 값 누적
                r_ += delta[i][j]
            if i + j == 99:        # 역대각선 값 누적
                l_ += delta[i][j]
                
        if row_ > max_sum:
            max_sum = row_
        if col_ > max_sum:
            max_sum = col_
        if r_ > max_sum:
            max_sum = r_
        if l_ > max_sum:
            max_sum = l_
            
        row_, col_ = 0, 0          # 행, 열 총 합 초기화