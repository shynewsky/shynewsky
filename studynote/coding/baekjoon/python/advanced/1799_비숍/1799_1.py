import sys
sys.stdin = open('input.txt')
from pprint import pprint

'''
방1) ㅡ 시간초과
백트래킹, 상태트리
'''

# 함수 ------------------------------------------------------------------

def recur(cnt, candidates): # cnt 깊이(비숍개수), candidate(다음에 놓을 수 있는 후보)
    global max_cnt

    if not candidates: # 종료조건 : 남은 후보군이 없을때
        if max_cnt < cnt:
            max_cnt = cnt
        return

    for candidate in candidates: # 후보군 마다, 다음 재귀의 후보군 새로 만들기
        x, y = candidate                  # 기준 후보
        new_candidates = candidates[:]    # 깊은 복사
        new_candidates.remove(candidate)  # 기준 후보도 다음 후보군에서 제거

        for d in range(4): # 가지치기 : 델타 순회로 대각선 4방향 제거

            while True:
                nx, ny = x+dx[d], y+dy[d]
                if not (0<=nx<N and 0<=ny<N): # 범위 벗어나면 방향전환
                    break
                if (nx, ny) in new_candidates: # 후보군에 있으면 제거
                    new_candidates.remove((nx, ny))
                x, y = nx, ny  # 다음 좌표 탐색을 위한 갱신

            if not new_candidates: # 후보군이 비어있으면
                break

        recur(cnt+1, new_candidates)

# 입력 ----------------------------------------------------------------
N = int(input()) # 10이하의 수 ㅡ 재귀 가능
board = [list(map(int, input().split())) for _ in range(N)]
'''
[[1, 1, 0, 1, 1],
 [0, 1, 0, 0, 0],
 [1, 0, 1, 0, 1],
 [1, 0, 0, 0, 0],
 [1, 0, 1, 1, 1]]
'''

# 변수 ------------------------------------------------------------------
candidates = [(i,j) for i in range(N) for j in range(N) if board[i][j]]
M = len(candidates) # 13
'''
[(0, 0), (0, 1), (0, 3), (0, 4), (1, 1), (2, 0), (2, 2), (2, 4), (3, 0), (4, 0), (4, 2), (4, 3), (4, 4)]
'''

# 코드 ------------------------------------------------------------------
# 상태트리가 그려지므로 - 백트래킹 사용
# candidate 를 모두 순회할때까지 재귀
# delta 로 candidate 가지치기

max_cnt = 0
dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]

recur(0, candidates)

print(max_cnt+1)
