import sys
sys.stdin = open('input.txt')

# 입력 --------------------------------------------------------------------------------------

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(M)]  # (x, y, color) 1-indexed
    # 바뀌지 않을 숫자는 tuple 로 해두면 인덱싱과 삭제 속도를 늘릴 수 있다

    # 변수 ----------------------------------------------------------------------------------

    # 보드 초기화 (0: 빈칸, 1: 흑, 2: 백)
    board = [[0]*N for _ in range(N)]
    mid = N // 2
    board[mid-1][mid-1] = 2
    board[mid-1][mid]   = 1
    board[mid][mid-1]   = 1
    board[mid][mid]     = 2

    # 개수 추적(빠른 출력용)
    cnt = {
        1: 2,
        2: 2,
    }

    # 8방향 (상,하,좌,우,대각선)
    # 바뀌지 않을 숫자는 tuple 로 해두면 인덱싱과 삭제 속도를 늘릴 수 있다
    delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # 코드 ----------------------------------------------------------------------------------

    for x, y, i in data:
        x -= 1  # 행
        y -= 1  # 열
        board[x][y] = i
        cnt[i] += 1

        # 상대색
        ni = 1 if i == 2 else 2

        # 8방향 검사
        for dx, dy in delta:
            nx, ny = x+dx, y+dy

            # 범위를 벗어났거나, 상대색이 아닌경우, 다른 방향으로 탐색시작
            if not (0<=nx<N and 0<=ny<N) or board[nx][ny] != ni:
                continue

            # 범위안에 있고, 상대색인 좌표들을 모두 모은다
            path = []
            while (0<=nx<N and 0<=ny<N) and board[nx][ny] == ni:
                path.append((nx, ny))
                nx += dx
                ny += dy

            # 상대색으로만 이루어진 경로로 가다가, 내 돌을 만나면, 사이에 있는 돌 모두 뒤집기
            if (0<=nx<N and 0<=ny<N) and board[nx][ny] == i and path:
                for fx, fy in path:
                    board[fx][fy] = i
                flipped = len(path)
                cnt[i]  += flipped
                cnt[ni] -= flipped

    # 출력 ----------------------------------------------------------------------------------

    print(f"#{t}", cnt[1], cnt[2])
