T = 10

for _ in range(1, T+1):

    # 입력
    test_case = int(input())
    N = 100
    matrix = [list(input()) for _ in range(N)]

    # 풀이
    max_len = 0

    # 행 순회
    for i in range(N): # 기준점 행 순회
        for j in range(N): # 기준점 열 순회

            length = 0
            for k in range(1,N+1): # 회문 길이 증가 (길이는 자연수)
                if j + k > N :
                    break
                if matrix[i][j:j+k] == matrix[i][j:j+k][::-1] :
                    length = k

            if max_len < length :
                max_len = length

    # 열 순회
    transpose = list(zip(*matrix))
    for i in range(N): # 기준점 행 순회
        for j in range(N): # 기준점 열 순회

            length = 0
            for k in range(1,N+1): # 회문 길이 증가 (길이는 자연수)
                if j + k > N :
                    break
                if transpose[i][j:j+k] == transpose[i][j:j+k][::-1] :
                    length = k

            if max_len < length :
                max_len = length

    # 출력
    print(f'#{test_case}', max_len)