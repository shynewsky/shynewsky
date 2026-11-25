dict = { # 파이프 모양별로 이동할 수 있는 방향을 저장한 딕셔너리
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],  # 상하좌우
    2: [(-1, 0), (1, 0)],   # 상하
    3: [(0, -1), (0, 1)],   # 좌우
    4: [(-1, 0), (0, 1)],   # 상우
    5: [(1, 0), (0, 1)],    # 하우
    6: [(1, 0), (0, -1)],   # 하좌
    7: [(-1, 0), (0, -1)],  # 상좌
}

T = int(input())
for t in range(1, T + 1):
    # 입력
    N, M, R, C, L = map(int, input().split())  # N행, M열, R행, C열, L시간
    matrix = [list(map(int, input().split())) for _ in range(N)] # 파이프 지도
    visited = [[0] * M for _ in range(N)] # 이동했을 수 있는 위치를 기록하는 지도

    # 풀이 (BFS)
    q = [[R, C]]
    visited[R][C] = 1
    count = 1

    while q:
        x, y = q.pop(0) # BFS

        if visited[x][y] >= L : # 가지치가 깊이 3이상이면 스탑
            continue

        for dx, dy in dict[matrix[x][y]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M \
                and matrix[nx][ny] != 0 \
                and visited[nx][ny] == 0\
                and (-dx, -dy) in dict[matrix[nx][ny]] : # 파이프끼리 연결되어있지 않으면 이동할 수 없게
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
                    count += 1

    # 출력
    print(f'#{t}', count)
