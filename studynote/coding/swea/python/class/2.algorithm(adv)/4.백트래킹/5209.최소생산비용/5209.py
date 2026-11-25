def recur(r, s):
    global min_sum

    if s > min_sum: # 가지치기
        return

    if r == N: # 종료조건
        if min_sum > s:
            min_sum = s
        return

    for c in range(N):
        if visited[c] == 1:
            continue
        visited[c] = 1
        recur(r+1, s+matrix[r][c])
        visited[c] = 0

T = int(input())
for t in range(1, T+1):
    # 입력
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 변수
    min_sum = float('inf')
    visited = [0] * N # 열 방문처리
    # 풀이
    recur(0, 0) # 0행, 총비용0
    # 출력
    print(f'#{t}',min_sum)

