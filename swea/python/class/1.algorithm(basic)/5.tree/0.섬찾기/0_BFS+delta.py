import sys
sys.stdin = open('input.txt')
from collections import deque

# 입력
N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 델타
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

# -------------------------------------------------------

# BFS
def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = True # 방문처리

    while q:
        r, c = q.popleft()

        for i in range(8):   # 8방향
            nr, nc = r+dr[i], c+dc[i]
    
            if 0<=nr<N and 0<=nc<M\
            and matrix[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))

# -------------------------------------------------------

island_cnt = 0 # 섬 개수
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            island_cnt += 1
            bfs(i,j)

# 출력
print(island_cnt)

