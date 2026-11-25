def recur(n):
    global min_val

    if n == N-1: # 1은 이미 들어가있기 때문에
        path.append(1)
        val = 0
        for i in range(N):
            val += mat[path[i]-1][path[i+1]-1]
        if min_val > val:
            min_val = val
        path.pop()
        return

    for i in range(2, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        path.append(i)
        recur(n+1)
        path.pop()
        visited[i] = 0

T = int(input())
for t in range(1, T+1):
    # 입력
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    # 변수
    min_val = float('inf') # int(21e8)를 쓰는 것보다 안전하고 범용적
    path = [1] # 사무실부터 출발하여, 관리구역을 선택하는 경로
    visited = [0] * (N+1)
    # 코드
    recur(0)
    # 출력
    print(f'#{t}', min_val)
