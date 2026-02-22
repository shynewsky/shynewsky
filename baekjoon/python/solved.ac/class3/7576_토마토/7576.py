import time
start = time.time()
# ---------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


M, N = map(int, input().split()) # 가로M,세로N
mat = [list(map(int, input().split())) for _ in range(N)] # 익은1, 안익은0, 없는-1

# 익은 토마토들로부터 퍼져나가는 구조
# - "익은 토마토들로부터" : Queue
# - "퍼져나가는 구조" : BFS (DFS보다 좋음)

# 1. 익은 토마토 Queue 만들기
q = deque()
for n in range(N):
    for m in range(M):
        if mat[n][m] == 1:
            q.append([n, m])

# 2. 퍼져나가는 BFS 구조
count = 0
delta = ((0,1), (0,-1), (1,0), (-1,0))
while q:
    cx, cy = q.popleft()

    for dx, dy in delta:
        nx, ny = dx + cx, dy + cy

        # 범위에서 나가면 넘어가기
        if not (0<=nx<N and 0<=ny<M):
            continue

        # 비어있거나(-1) 익었으면(1) 넘어가기
        if mat[nx][ny] != 0:
            continue

        mat[nx][ny] = mat[cx][cy] + 1
        q.append([nx, ny])

# 3. 모두 익었는지 확인
# - 모든 토마토가 익었으면(0이 없으면) 0
# - 모두 익지 못하는 상황이면(0이 있으면) -1

max_val = 0
isZero = False
for n in range(N):
    for m in range(M):
        if mat[n][m] == 0:
            isZero = True
            break
        if max_val < mat[n][m]:
            max_val = mat[n][m]
    if isZero:
        print(-1)
        break
else:
    print(max_val - 1)

# ---------------------
end = time.time()
print(end-start,'초')