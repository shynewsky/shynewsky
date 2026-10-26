T = 10

for test_case in range(1, T+1):

    # 입력
    N = int(input()) # 항상 100
    matrix = [list(map(int, input().split())) for _ in range(N)] # 100*100
    transpose = list(zip(*matrix))

    # 코드
    # 전치행렬에서, 2 1 을 ( ) 로 보자
    count = 0

    for i in range(N): # 행 순회
        last_num = 0 # 행 바뀌면 초기화

        for j in range(N): # 열 순회

            if transpose[i][j] == 1 : # 2일때 저장해놓고
                last_num = 1
                # print(i, j, matrix[i][j], count)

            elif last_num == 1 and transpose[i][j] == 2 : # 이후에 1 발견하면
                count += 1   # 21 쌍 추가
                last_num = 0 # 다음 2를 찾을 수 있게 초기화
                # print(i, j, matrix[i][j], count, '---')

    print(f'#{test_case}', count)
