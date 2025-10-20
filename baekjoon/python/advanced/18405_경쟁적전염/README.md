## 1️⃣ 내 코드

```python
# 입력 -----------------------------------------------------------------
N, K = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 변수 -----------------------------------------------------------------

# mat를 모두 탐색해서 다 채워졌는지 확인하지 말고, 채워질때마다 개수 줄이기
cnt_zero = N*N

# dict 로 델타 탐색하고, mat 에 바이러스 기록
dict = {i:[] for i in range(1, K+1)}
for i in range(N):
    for j in range(N):
        if mat[i][j]: # 0 말고
            dict[mat[i][j]].append([i, j])
            cnt_zero -= 1

# print(dict)

# 인덱싱이 언패킹보다 미세하게나마 빠르므로 델타 좌표를 나눈다
# delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 코드 -----------------------------------------------------------------

v = 0               # 나눗셈 연산으로 인덱스가 될 예정
is_found = False    # 답을 찾았을때 반복문을 탈출하기 위한 변수

while True:     # 처음부터 모든 값이 채워져있는 경우, 루프를 돌지 않는다

    if not cnt_zero: # 가지치기 : 꽉찼을때
        break

    if is_found: # 가지치기 : 값 찾았을때
        break

    if v == S*K: # 종료조건 : S초가 넘었을때
        break

    val = v % K + 1
    q = dict[val][::]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and mat[nx][ny]==0:
                if nx+1 == X and ny+1 == Y:
                    is_found = True
                mat[nx][ny] = val
                dict[val].append([nx, ny])
                cnt_zero -= 1
    v += 1

answer = mat[X-1][Y-1]  # 없으면 0, 채워지면 해당 값이 될 예정

# for row in mat:
#     print(row)

# 출력 -----------------------------------------------------------------

print(answer)
```
<hr>

## 2️⃣ 시간복잡도 분석

- 초기 스캔 : O(N^2)
- q = dict[val][::] : O(S * N^2)
- q.pop(0) : O(L^2)
- v == S*K : 불필요한 반복


- 개선방법 : 리스트 복사 제거, pop(0) 제거 

<hr>

## 3️⃣ 효율적인 코드

### 다중시작점 BFS & deque

- 모든 초기 바이러스 좌표를 (time, virus, x, y) 한 큐에 넣고 정렬

```python
from collections import deque
import sys

input = sys.stdin.readline

# 입력
N, K = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 초기 바이러스 수집: (virus, x, y) 모아서 번호 순 정렬
viruses = []
for i in range(N):
    for j in range(N):
        if mat[i][j] != 0:
            viruses.append((mat[i][j], i, j))

viruses.sort(key=lambda v: v[0])  # 바이러스 번호 오름차순

# 다중 시작점 BFS 큐: (time, virus, x, y)
q = deque((0, v, x, y) for v, x, y in viruses)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# BFS
while q:
    t, v, x, y = q.popleft()
    if t == S:      # S초가 되면 더 이상 확산하지 않음
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and mat[nx][ny] == 0:
            mat[nx][ny] = v
            q.append((t + 1, v, nx, ny))
            # (X-1, Y-1)이 채워졌고 t+1 <= S이면 조기 종료 가능
            if nx == X - 1 and ny == Y - 1 and t + 1 <= S:
                # 큐를 비워도 되고, 곧바로 답 출력로 넘어가도 됨
                q.clear()
                break

print(mat[X-1][Y-1])
```
