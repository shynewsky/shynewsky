## 1️⃣ 내 코드

30개 중 10개 통과 (20개 틀림)

틀린 이유 (예상):

내가 오셀로 규칙을 제대로 이해하지 못하고 있는 것 같다. 
자신과 자신 사이에 있는 모든 상대의 돌을 뒤집을 수 있는걸로 생각했는데, 
그래서 틀렸다..(?)고 한다

- 총 시간복잡도 : O(M * N^3)

```python
import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 입력 ---------------------------------------------------------------------------------------
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # N 행/열 수, M 돌 놓는 횟수
    data = [list(map(int, input().split())) for _ in range(M)] # (x, y) color

    # 변수 -----------------------------------------------------------------------------------

    # 보드 초기화
    mat = [[0] * N for _ in range(N)]
    mat[N//2-1][N//2-1], mat[N//2-1][N//2], mat[N//2][N//2-1], mat[N//2][N//2] = 2, 1, 1, 2

    # 흑백 좌표 저장
    dict = {
        1 : [[N//2-1, N//2], [N//2, N//2-1]],
        2 : [[N//2-1, N//2-1], [N//2, N//2]],
    }

    # 흑백 개수 초기화
    cnt_1 = cnt_2 = 2 # black, white

    # 8방향 - 변경되는 변수가 아니면 튜플이 리스트보다 빠르다(?)
    delta = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

    # 코드 -----------------------------------------------------------------------------------

    # - 다음에 놓을 좌표를 받아온다
    # - 같은 색상의 돌 좌표를 확인하고, 해당 좌표까지의 방향벡터를 구한다
    # - 방향벡터로 이동하며 반대 색상은 반전시키고, 돌 개수도 갱신한다

    for a, b, i in data:

        # 인덱스로 변환
        x, y = a-1, b-1

        # 돌 올리기
        mat[x][y] = i

        # 돌 개수 추가
        if i == 1:
            cnt_1 += 1
        else:
            cnt_2 += 1

        # 루프돌면 dict[i] 리스트에 추가할 좌표들
        new_stone = [[x, y]]

        # 1일때 2, 2일때 1로 색상 전환
        # 2//i 를 하면 i=1 일때 2, i=2일때 1이 된다
        ni = 2//i

        for nx, ny in dict[i]: # 같은 색상의 다른 돌 좌표 가져오기

            # 방향벡터 구하기
            dx, dy = nx-x, ny-y

            if dx != 0 :
                d = abs(dx) # 음수대비
                dx, dy = dx/d, dy/d
            elif dy != 0 : # dx == 0
                d = abs(dy) # 음수대비
                dx, dy = dx/d, dy/d

            # 8방향이 아니면 스킵
            if (dx, dy) not in delta:
                continue

            # 나누면서 float 가 되어서 다시 int 로 바꿔야 인덱스로 동작할 수 있다
            dx, dy = int(dx), int(dy)

            # 현재위치 좌표
            cx, cy = x, y

            # 가는길에 0이 있는지 확인하기
            isZero = False
            while cx+dx != nx or cy+dy != ny:

                # 현재 좌표이동
                cx += dx
                cy += dy

                if mat[cx][cy] == 0:
                    isZero = True
                    break

            if isZero: # 하나라도 있으면 다음 타겟으로 변경
                continue

            # 현재위치 좌표(다시 받아오기)
            cx, cy = x, y

            # 같은 색상의 다른 돌 좌표에 도달할때까지 이동
            while cx+dx != nx or cy+dy != ny:

                # 현재 좌표이동
                cx += dx
                cy += dy

                if mat[cx][cy] == i:
                    break

                # 색상 다르면 바꾸기
                if mat[cx][cy] == ni: # 색상이 다르면
                    mat[cx][cy] = i   # 색상 반전
                    dict[ni].remove([cx, cy])   # 반대 색상에서 제거
                    new_stone.append([cx, cy])  # 바꾼 색상에 추가

                    # 개수 조절
                    if i == 1:
                        cnt_1 += 1
                        cnt_2 -= 1
                    else:
                        cnt_1 -= 1
                        cnt_2 += 1

            # 다음 이동을 위해 좌표 원위치
            cx, cy = x, y

        # 새로 추가된 돌 위치 추가
        dict[i] += new_stone

    # 출력 ---------------------------------------------------------------------------
    print(f'#{t}', cnt_1, cnt_2)
```

### 내가 틀렸던 부분

1. 0을 만나면 안되는 부분
```python
            # 현재위치 좌표
            cx, cy = x, y

            # 가는길에 0이 있는지 확인하기
            isZero = False
            while cx+dx != nx or cy+dy != ny:

                # 현재 좌표이동
                cx += dx
                cy += dy

                if mat[cx][cy] == 0:
                    isZero = True
                    break

            if isZero: # 하나라도 있으면 다음 타겟으로 변경
                continue
```

2. 같은 색을 만나면 끊어야 하는 부분

```python
                if mat[cx][cy] == i:
                    break
```

<hr>

## 2️⃣ 효율적인 코드

- 시간 복잡도 : O(M * N)

```python

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
```









