import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(N)]

    # start = [[i,j] for i in range(N) for j in range(N) if matrix[i][j] == 2] # [[4, 3]]
    start = next(([i, j] for i in range(N) for j in range(N) if matrix[i][j] == 2), []) # [4, 3]
    s = [start]
    visited = [[0] * N for _ in range(N)]
    ok = False

    while s:
        x, y = s.pop()

        if matrix[x][y] == 3: # 탈출조건
            ok = True

        if visited[x][y] == 0: # 방문하지 않았으면
            visited[x][y] = 1 # 방문 표시

            for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]: # 다음 노드 검색
                nx, ny = x + dx, y + dy

                if 0<=nx<N and 0<=ny<N and matrix[nx][ny] != 1 and visited[nx][ny] == 0:
                    s.append([nx,ny])

    print(f'#{test_case}', int(ok))

