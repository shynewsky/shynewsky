import sys
sys.stdin = open('input.txt')

'''
분기한정 백트래킹(Branch & Bound)
- Branch : 해 공간을 나누어 탐색하되
- Bound : 최대/최소 성과의 상한/하한을 계산해 가망 없는 가지를 자르는 전략
- 백트래킹 + @ 로 "가능성이 있어도 더 좋아질 여지가 없음" 도 잘라낸다

흑백분리
- 검은색 칸에 놓인 비숍은 오직 다른 검은색 칸에 놓인 비숍만 공격할 수 있다
- 하얀색 칸에 놓인 비숍은 오직 다른 하얀색 칸에 놓인 비숍만 공격할 수 있다

- 1) 검정 칸에 놓을 수 있는 최대 비숍 수 계산
- 2) 흰색 칸에 놓을 수 있는 최대 비숍 수 계산
'''
'''
# BB 기본 코드

best = 0  # 지금까지 찾은 최고 기록

def dfs(level, score):
    global best

    # 가지치기 (더 가봐야 소용없는 경우)
    if score + (남은칸수) <= best:
        return

    # 끝까지 탐색한 경우
    if level == N:
        best = max(best, score)
        return

    # 이번 칸에 무언가를 한다
    dfs(level + 1, score + 1)
    # 이번 칸을 그냥 넘긴다
    dfs(level + 1, score)
'''
'''
# 비숍문제 간단 버전 코드

def dfs(idx, count):
    global best
    if count + (남은대각선수) <= best:
        return

    if idx == 대각선끝:
        best = max(best, count)
        return

    # 이번 대각선에 놓을 수 있으면
    for 자리 in 가능한자리[idx]:
        if not 부딪힘[자리]:
            부딪힘[자리] = True
            dfs(idx + 1, count + 1)
            부딪힘[자리] = False

    # 이번 대각선엔 안 놓는 경우
    dfs(idx + 1, count)
'''

import sys
sys.setrecursionlimit(10 ** 6) # 재귀 깊이 제한 증가 (백트래킹 사용 시 필요)

# 전역 변수 설정
N = 0
board = []
diag_right = []      # ↗ 방향 대각선: r + c (0 ~ 2*N-2)
diag_left = []       # ↖ 방향 대각선: r - c + N - 1 (0 ~ 2*N-2)
max_bishops = [0, 0] # [0: 검은색 칸 최대, 1: 흰색 칸 최대]

def dfs(idx, count, color):
    """
    비숍을 놓는 백트래킹 함수
    idx: 현재 탐색할 칸의 인덱스 (0부터 N*N-1)
    count: 현재까지 놓은 비숍 수
    color: 0 (검은색 칸) 또는 1 (흰색 칸)
    """
    global N, board, diag_right, diag_left, max_bishops

    if idx == N * N: # 모든 칸 탐색 완료
        max_bishops[color] = max(max_bishops[color], count)
        return

    r, c = idx//N, idx%N # 현재 칸의 색깔: (r+c)%2. (검은색: 0, 흰색: 1)

    # 1. 현재 탐색 색깔(color)과 칸의 색깔이 일치하는 경우
    if (r + c) % 2 == color:
        if board[r][c] == 1:  # 비숍을 놓을 수 있는 칸이고
            if not diag_right[r + c] and not diag_left[r - c + N - 1]: # 대각선 충돌 체크

                # 1-1. 비숍을 놓는 경우
                diag_right[r + c] = True
                diag_left[r - c + N - 1] = True

                # 다음 칸 탐색
                dfs(idx + 1, count + 1, color)

                # 백트래킹: 상태 복원
                diag_right[r + c] = False
                diag_left[r - c + N - 1] = False

        # 1-2. 비숍을 놓지 않는 경우 (board[r][c] == 0 이거나, 놓을 수 있지만 안 놓는 경우)
        dfs(idx + 1, count, color)

    # 2. 현재 탐색 색깔과 칸의 색깔이 다른 경우 (다른 색깔 칸)
    else:
        dfs(idx + 1, count, color) # 다음 칸으로 넘어간다 (count에 영향을 주지 않음)


def solve():
    global N, board, diag_right, diag_left

    # 입력 처리 및 전역 변수 초기화
    try:
        N = int(sys.stdin.readline())
        for _ in range(N):
            board.append(list(map(int, sys.stdin.readline().split())))

    except:
        print(0)
        return

    # 대각선 배열 크기 초기화
    diag_size = 2 * N - 1

    # === 1. 검은색 칸 탐색 (color=0) ===
    # 상태 배열 초기화
    diag_right = [False] * diag_size
    diag_left = [False] * diag_size
    dfs(0, 0, 0)

    # === 2. 흰색 칸 탐색 (color=1) ===
    # 상태 배열 초기화 (다시)
    diag_right = [False] * diag_size
    diag_left = [False] * diag_size
    dfs(0, 0, 1)

    # 결과 출력
    print(max_bishops[0] + max_bishops[1])

solve()
