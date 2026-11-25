# 백트래킹

- 백트래킹 (최악의 수로 하면, 터진다) 🤖

```python
import sys
sys.stdin = open('input.txt')

def recur(n):
    global max_cnt, min_num

    if n == 0: # 시작점일때
        for i in range(N): # 기준점 행 순회
            for j in range(N): # 기준점 열 순회
                path.append([i, j])
                recur(n+1)
                path.pop()

    else: # 시작점이 아닐때
        isMoved = False
        for di, dj in delta:
            i, j = path[-1]
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N: # 범위 안에 있으면
                if matrix[ni][nj] == matrix[i][j] + 1: # 다음칸이 있으면 이동
                    isMoved = True
                    path.append([ni,nj])
                    recur(n+1)
                    path.pop()

        if not isMoved:
            num = matrix[path[0][0]][path[0][1]]
            if (n > max_cnt) or (n == max_cnt and num < min_num):
                max_cnt = n
                min_num = num

T = int(input())
for t in range(1, T+1):
    # 입력
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 변수
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우
    path = []
    max_cnt = 0
    min_num = float('inf')
    # 풀이
    recur(0) # 0개부터 시작
    # 출력
    print(f'#{t}', min_num, max_cnt)
```