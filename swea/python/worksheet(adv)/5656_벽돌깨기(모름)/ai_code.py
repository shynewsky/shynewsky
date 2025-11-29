import sys
from collections import deque
input = sys.stdin.readline

# 4방향
DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

def count_bricks(board):
    return sum(1 for row in board for v in row if v)

def first_hit_row(board, c, H):
    for r in range(H):
        if board[r][c] != 0:
            return r
    return -1

def boom(board, sr, sc, H, W):
    """(sr, sc)에서 시작해 BFS로 폭발. 값 k는 사방으로 k-1칸까지 전파."""
    if sr < 0:
        return
    q = deque()
    q.append((sr, sc, board[sr][sc]))
    visited = [[False]*W for _ in range(H)]
    visited[sr][sc] = True

    # 폭파 대상 수집 후 한 번에 0으로 만드는 방식
    to_zero = []

    while q:
        r, c, power = q.popleft()
        if board[r][c] == 0:
            continue
        to_zero.append((r, c))
        # power가 1이면 자기 자신만 파괴, >1이면 전파
        if power > 1:
            for d in range(4):
                for step in range(1, power):
                    nr = r + DR[d]*step
                    nc = c + DC[d]*step
                    if not (0 <= nr < H and 0 <= nc < W):
                        break
                    if board[nr][nc] == 0:
                        continue
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc, board[nr][nc]))

    for r, c in to_zero:
        board[r][c] = 0

def apply_gravity(board, H, W):
    for c in range(W):
        stack = []
        # 아래에서 위로 모으기
        for r in range(H-1, -1, -1):
            if board[r][c] != 0:
                stack.append(board[r][c])
        # 다시 아래부터 채우기
        idx = H-1
        for v in stack:
            board[idx][c] = v
            idx -= 1
        # 나머지는 0
        for r in range(idx, -1, -1):
            board[r][c] = 0

def shoot(board, col, H, W):
    """col 열에 공을 떨어뜨려 한 번의 시뮬레이션을 수행"""
    r = first_hit_row(board, col, H)
    if r == -1:
        return  # 이 열은 아무 일도 안 생김
    boom(board, r, col, H, W)
    apply_gravity(board, H, W)

def solve_case(N, W, H, origin):
    best = float('inf')

    def dfs(depth, board):
        nonlocal best
        remain = count_bricks(board)
        if remain == 0:
            best = 0
            return
        if depth == N:
            if remain < best:
                best = remain
            return
        # 간단 가지치기: 현재 남은 게 이미 best 이하로 못 줄일 것 같으면… (보수적으로 둠)
        if remain >= best:
            # 더 던져서 줄일 수 있긴 하지만, 남은 공이 적고 best가 0에 가깝다면 의미가 적음
            pass

        # 유효한(맨 위가 비어있지 않은) 열만 시도
        tried_any = False
        for c in range(W):
            top = first_hit_row(board, c, H)
            if top == -1:
                continue
            tried_any = True
            nb = [row[:] for row in board]
            shoot(nb, c, H, W)
            dfs(depth + 1, nb)
            if best == 0:  # 최적
                return

        # 모든 열이 비었는데 depth < N 인 경우: 더 던져도 변화 없음
        if not tried_any:
            if remain < best:
                best = remain
            return

    dfs(0, [row[:] for row in origin])
    return 0 if best == float('inf') else best

# -------------------- main --------------------
if __name__ == "__main__":
    T = int(input().strip())
    for tc in range(1, T+1):
        N, W, H = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(H)]
        ans = solve_case(N, W, H, board)
        print(f"#{tc} {ans}")
