import sys
sys.stdin = open('input.txt')
from pprint import pprint

'''
방2) ㅡ 오류
회의실 예약하듯이, 하나 선택하면 연결된 모든 대각선의 후보군을 지운다
'''

# 입력 ----------------------------------------------------------------
N = int(input()) # 10이하의 수 ㅡ 재귀 가능
board = [list(map(int, input().split())) for _ in range(N)]

# 변수 ------------------------------------------------------------------
candidates = [(i,j) for i in range(N) for j in range(N) if board[i][j]]
M = len(candidates) # 13

# 코드 ------------------------------------------------------------------

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]

for candidate in candidates:
    for d in range(4):  # 가지치기 : 델타 순회로 대각선 4방향 제거
        x, y = candidate  # 기준 후보

        while True:
            nx, ny = x + dx[d], y + dy[d]
            if not (0<=nx<N and 0<=ny<N): # 범위 벗어나면 방향전환
                break
            if (nx, ny) in candidates:  # 후보군에 있으면 제거
                candidates.remove((nx, ny))

            x, y = nx, ny  # 다음 좌표 탐색을 위한 갱신

print(len(candidates))
