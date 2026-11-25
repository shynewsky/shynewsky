def recur(i, summary):
    global min_sum
    
    if min_sum < summary: # 가지치기
        return
    
    if i == N: # [N-1]행까지 있으므로, [N]행이면 종료
        if min_sum > summary:
            min_sum = summary
        return
    
    for j in range(N): # [N-1]열까지 있음
        if visited[j] == 1:
            continue
        visited[j] = 1
        recur(i+1, summary+matrix[i][j]) # 다음행 찾기
        visited[j] = 0
    
T = int(input()) # 테스트케이스
for t in range(1, T+1):
    # 입력
    N = int(input()) # 행/열 수
    matrix = [list(map(int, input().split())) for _ in range(N)] # 행렬 받기
    # 변수
    path = []
    min_sum = float('inf')
    visited = [0] * N # 방문한 열 표시
    # 재귀
    recur(0, 0) # 0행부터 시작, 합 0부터 시작
    # 출력
    print(f'#{t}', min_sum)