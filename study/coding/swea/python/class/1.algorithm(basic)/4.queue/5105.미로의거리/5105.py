from collections import deque

T = int(input()) # 테스트케이스 수

for test_case in range(1, T+1):

    N = int(input()) # 행/열 수
    matrix = [list(map(int, input())) for _ in range(N)]

    x, y = next((i, j) for i in range(N) for j in range(N) if matrix[i][j] == 2)
    q = deque() # 큐 초기화
    visited = [[0] * (N) for _ in range(N)] # 방문 여부 리스트
    visited[x][y] = 1   # 시작노드 방문 처리
    q.append([x, y])    # 큐에 삽입

    # 탐색
    while q : # 큐에 원소가 있을때
        x, y = q.popleft() # 맨 앞에서 원소 제거

        # 탈출조건
        if matrix[x][y] == 3 :
            print(f'#{test_case}', visited[x][y] -2)
            break

        # 델타
        for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]] : # 방향벡터 꺼내기
            nx, ny = x + dx, y + dy

            if 0<=nx<N and 0<=ny<N and matrix[nx][ny] != 1 and visited[nx][ny] == 0 :
                visited[nx][ny] = visited[x][y] + 1  # visitied 에 거리를 누적하기
                q.append([nx, ny])  # 이동하는게 아니라, 큐에 추가하기
    else :
        print(f'#{test_case}', 0)
