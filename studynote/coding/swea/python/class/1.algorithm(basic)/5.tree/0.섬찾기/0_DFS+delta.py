import sys
sys.stdin = open('input.txt')

# 입력
N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 델타
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

# -------------------------------------------------------

# DFS
def dfs(r, c):
    visited[r][c] = True # 방문처리
    for i in range(8):   # 8방향
        nr, nc = r+dr[i], c+dc[i]

        if 0<=nr<N and 0<=nc<M\
        and matrix[nr][nc] == 1 and not visited[nr][nc]:
            dfs(nr, nc)

# -------------------------------------------------------

island_cnt = 0 # 섬 개수
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            island_cnt += 1
            dfs(i,j)

# 출력
print(island_cnt)
