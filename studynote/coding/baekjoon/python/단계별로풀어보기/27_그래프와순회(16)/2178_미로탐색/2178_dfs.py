# 타이머
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
from pprint import pprint as pp
from collections import deque
# -------------------------------

# 입출력
N, M = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(N)]

# 코드
# stack, queue, deque 중 주로 queue/deque 를 많이 씀
# stack 은 pop()만 있어서, 뒤에서부터 꺼내려면 정렬해야해서
# 그래프 문제에서는 queue/deque 를 사용하는 BFS 를 쓸 예정

q = deque()
q.append([0, 0])

# DFS 는 "pop할떄 방문처리"
# - 방문 안 한 노드로 가기 떄문에 조금이라도 늦으면 중복 visit
# BFS 는 "append할떄 방문처리"
# - 방문 안 한 노드를 큐에 넣어서 조금이라도 늦으면 중복 append
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

# 인접한 칸 이동가능 = 델타 (1,0)(-1,0)(0,1)(0,-1)
delta = [(0,-1), (0,1), (-1,0), (1,0)]

while q:
    cx, cy = q.popleft()

    # 현재 칸 기준으로 인접한 1들 모두 큐에 넣기
    for dx, dy in delta:
        nx, ny = cx + dx, cy + dy

        # 범위에 없으면 패스
        if not(0<=nx<N and 0<=ny<M):
            continue

        # 1이 아니어도 패스
        if mat[nx][ny] == 0:
            continue

        # 방문했었으면 패스
        if visited[nx][ny] != 0:
            continue

        q.append([nx, ny])
        # visited[nx][ny] = 1
        # 거리를 count 로 올리는게 아니라 visited 행렬로 파악
        visited[nx][ny] = visited[cx][cy] + 1

print(visited[N-1][M-1])

# 타이머
end = time.time()
print(end-start, '초')