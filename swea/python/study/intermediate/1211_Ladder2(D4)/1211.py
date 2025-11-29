T = 10  # 테스트 케이스 수

for _ in range(1, T+1):

    # 입력
    test_case = int(input()) # 테스트케이스 번호
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)] # 100*100 행렬

    # 풀이
    # 시작점이 될 수 있는 곳을 모두 찾는다
    start = [[0, j] for j in range(N) if matrix[0][j] == 1]

    # 델타 - 방향벡터 리스트를 만든다
    delta = [[0, -1], [0, 1], [1, 0]] # 좌, 우, 하 (우선순위 순서대로. 갈길이 있으면 바로 가버릴것이다)

    # 사다리타기
    min_count = N*N # 가장 큰 수로 초기화해놓고 최솟값 갱신하기
    min_y = 0 # 최소 이동거리의 열 좌표

    for x, y in start: # 시작점 하나 잡고
        count = 0
        cur_y = y
        
        while x < N-1 : # 바닥에 닿을때까지 진행

            for dx, dy in delta : # 방향벡터 꺼내서
                nx, ny = x + dx, y + dy # 다음 이동할 좌표 구하고

                if 0<=nx<N and 0<=ny<N and matrix[nx][ny]==1 : # 해당 좌표가 유효하면
                    matrix[x][y] = 2 # 내가 있던 자리를 2 로 바꾸고
                    x, y = nx, ny    # 좌표를 이동한다
                    count += 1       # 이동 횟수를 증가한다
                    break

        # 이동을 완료했으면, 최솟값을 비교하여 갱신하고
        if min_count > count :
            min_count = count
            min_y = cur_y

        # 2로 작성해 놓은 모든 좌표를 다시 1로 돌려놓는다
        for i in range(N): # 행 번호
            for j in range(N): # 열 번호
                if matrix[i][j] == 2:
                    matrix[i][j] = 1

    # 출력
    print(f'#{test_case}', min_y)


