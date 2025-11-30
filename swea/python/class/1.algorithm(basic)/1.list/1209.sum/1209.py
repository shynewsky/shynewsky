T = 10 # 테스트 케이스 수

for _ in range(1, T+1):

    # 입력
    test_case = int(input())
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 변수
    sum_list = []

    # 행의 합을 한꺼번에 계산
    sum_list.extend([sum(row) for row in matrix])

    # 열의 합을 한꺼번에 계산 - zip() 활용
    sum_list.extend([sum(col) for col in zip(*matrix)])

    # 대각선의 합을 구하여 하나씩 추가
    diagonal1 = sum(matrix[i][i] for i in range(N))
    diagonal2 = sum(matrix[i][N - 1 - i] for i in range(N))
    sum_list.append(diagonal1)
    sum_list.append(diagonal2)

    # 출력
    print(f'#{test_case} {max(sum_list)}')