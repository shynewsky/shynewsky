import time
start = time.time()
# -------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint

# Union-Find 는 부적합 -> 일차원 간선 그래프에서 사용
# DFS/BFS 로 덩어리 탐색 -> 방문 안한 1 발견시, cnt++ 후 DFS/BFS 실행

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # 밭 크기, 배추 개수
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split()) # 배추 위치
        graph[Y][X] = 1

    # BFS
    q = deque()
    visited = [[0] * M for _ in range(N)] # 방문표시
    delta = ((0, 1), (0, -1), (1, 0), (-1, 0)) # 상하좌우
    count = 0

    # 전체 순회
    for r in range(N):  # 행 순회
        for c in range(M): # 열 순회

            # 배추 없으면 넘기기
            if graph[r][c] != 1:
                continue

            # 방문한 덩어리면 넘기기
            if visited[r][c] == 1:
                continue

            # 시작점 큐에 등록
            q.append([r, c])
            visited[r][c] = 1
            count += 1

            # 부분 순회
            while q:
                cr, cc = q.popleft()

                for dr, dc in delta:
                    nr, nc = cr + dr, cc + dc

                    # 범위 벗어나면 패스
                    if not (0<=nr<N and 0<=nc<M):
                        continue

                    # 배추 없으면 패스
                    if graph[nr][nc] != 1:
                        continue

                    # 방문했으면 패스
                    if visited[nr][nc] == 1:
                        continue

                    q.append([nr, nc])
                    visited[nr][nc] = 1

    print(count)

# -------------------
end = time.time()
print(end-start, '초')