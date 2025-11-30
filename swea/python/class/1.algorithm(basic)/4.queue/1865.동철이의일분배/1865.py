def recur(i,s):
    global max_sum

    if max_sum >= s: # 가지치기
        return

    if i == N: # 종료조건
        if max_sum < s:
            max_sum = s
        return

    for j in range(N):
        if visited[j] == 1:
            continue
        visited[j] = 1
        recur(i+1, s*matrix[i][j]/100)
        visited[j] = 0

T = int(input())
for t in range(1, T+1):
    # 입력
    N = int(input()) # 행/열 수
    matrix = [list(map(float, input().split())) for _ in range(N)] # 확률표
    # 변수
    max_sum = 0
    visited = [0] * N # 열 방문횟수(일 선택여부)
    # 풀이
    recur(0,1) # 0행(0번사람), 확률1
    # 출력
    print(f'#{t} {max_sum*100:.6f}')
