T = int(input())
for test_case in range(1, T+1):

    # 입력
    N, M = map(int,input().split()) # N행 M열
    matrix = [list(input().strip()) for _ in range(N)]

    # 일단 첫번째 행과 마지막 행은 W 와 R 로 색칠 ㅡ 이건 기본으로 갖고 가는 개수
    cnt = 0
    cnt += M - matrix[0].count('W') # W 가 아닌 개수 더하기
    cnt += M - matrix[-1].count('R') # R 이 아닌 개수 더하기

    # 기본 수정 값을 제외한 행렬 다시 만들기
    mid_matrix = matrix[1:-1]

    # 1행만 남은 경우 ㅡ 반드시 B로 채워야함
    # 2행이 남은 경우 ㅡ W/B, B/R, B 로 채울 수 있음
    # 3행이상 남은 경우 ㅡ W/B/R, W/B, B/R, B 로 채울 수 있음

    if len(mid_matrix) == 1:
        cnt += M - mid_matrix[0].count('B')
    elif len(mid_matrix) == 2:
        sum1 = (M - mid_matrix[0].count('W')) + (M - mid_matrix[1].count('B'))
        sum2 = (M - mid_matrix[0].count('B')) + (M - mid_matrix[1].count('B'))
        sum3 = (M - mid_matrix[0].count('B')) + (M - mid_matrix[1].count('R'))
        cnt += min([sum1, sum2, sum3])
    else:
        min_sum = N * M
        length = len(mid_matrix)
        for i in range(0, length-1): # 파랑이 시작할 수 있는 인덱스
            for j in range(i+1, length): # 파랑이 끝날 수 있는 인덱스

                sum1 = ((M*i) - sum(row.count('W') for row in mid_matrix[:i])) if mid_matrix[:i] != [] else 0
                sum2 = ((M*(j-i)) - sum(row.count('B') for row in mid_matrix[i:j]))
                sum3 = ((M*(length-j)) - sum(row.count('R') for row in mid_matrix[j:])) if mid_matrix[j:] != [] else 0
                temp_sum = sum1 + sum2 + sum3

                if min_sum > temp_sum:
                    min_sum = temp_sum

        cnt += min_sum

    print(f"#{test_case}", cnt)