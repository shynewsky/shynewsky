import sys
sys.stdin = open('input.txt')

def recur(r, c):
    global min_sum

    if r == c == 0:
        path.append(matrix[r][c])  # 경로에 추가

    if sum(path) > min_sum: # 가지치기
        return

    if r == c == N-1: # 종료조건: (N-1, N-1)일때
        if min_sum > sum(path):
            min_sum = sum(path)
        return

    for dr, dc in delta:
        nr, nc = r+dr, c+dc         # 다음 좌표가
        if 0<=nr<N and 0<=nc<N:     # 범위 안에 있을때
            # visited[r][c] = 1       # 현재위치 방문 표시
            path.append(matrix[nr][nc]) # 경로에 추가
            recur(nr, nc)           # 다음 칸으로 이동
            path.pop()              # 돌아올라가지 못함
            # visited[r][c] = 0       # 방문표시 취소

T = int(input()) # 테스트케이스 수
for test_case in range(1, T+1):
    # 입력
    N = int(input()) # 행/열 수
    matrix = [list(map(int, input().split())) for _ in range(N)] # 숫자판
    # 변수
    path = [] # 바구니
    # visited = [[0] * (N) for _ in range(N)] # 방문표시
    delta = [[0,1],[1,0]] # 오른쪽, 아래쪽
    min_sum = float('inf')
    # 재귀
    recur(0,0) # 시작점 (0,0)
    # 출력
    print(f'#{test_case}', min_sum)

