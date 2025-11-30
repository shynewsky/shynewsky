import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 함수 ---------------------------------------------------------------------
def recur(stack, cnt, visited, chance):
    global max_cnt

    # 종료조건
    # 항상 stack+[(nx, ny)]로 넘겨주기 때문에 비어있는 경우가 없다
    # if not stack: # 비면 종료
    #     print('done')
    #     return

    if max_cnt < cnt:
        max_cnt = cnt

    x, y = stack.pop()
    current_node = mat[x][y] # 현재 높이
    # print((x, y), current_node, cnt)

    if not visited[x][y]: # 방문하지 않았다면

        for dx, dy in delta: # 사방향 탐색
            nx, ny = x+dx, y+dy # 다음 좌표 계산

            if not (0<=nx<N and 0<=ny<N): # 범위 밖이면 스킵
                continue

            if visited[nx][ny]: # 방문했었으면
                continue

            next_node = mat[nx][ny] # 다음 높이

            # 현재 높이 미만일때, 바로 stack 에 추가
            if next_node < current_node:

                visited[x][y] = 1  # 방문표시
                recur(stack+[(nx, ny)], cnt+1, visited, chance)
                visited[x][y] = 0  # 방문표시

            # 현재 높이 이상일때, 차가 K보다 작고, 깍은 후에도 0보다 크고, 깍을 횟수가 남아있다면
            # => 깎은 후 추가
            elif next_node - (current_node - 1) <= K and chance:
                mat[nx][ny] = current_node - 1

                visited[x][y] = 1  # 방문표시
                recur(stack+[(nx, ny)], cnt+1, visited, chance-1)
                visited[x][y] = 0 # 방문표시

                mat[nx][ny] = next_node

# 입력 -----------------------------------------------------------------
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split()) # N 한변길이(3<=N<=8), K 최대깎는높이(1<=K<=5) : 수가 작으므로 재귀 가능
    mat = [list(map(int, input().split())) for _ in range(N)] # 지도

    # 코드 -------------------------------------------------------------------

    # 지도 내에서 최댓값 찾기
    max_height = max([max(row) for row in mat])

    # 최댓값이 해당하는 좌표 찾기
    s = [(i, j) for i in range(N) for j in range(N) if mat[i][j] == max_height]

    # 방문기록용
    visited = [[0] * N for _ in range(N)]

    # 전역변수
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))  # (상하좌우) 고정변수는 튜플이 속도가 더 빠르다
    max_cnt = 0  # 최대 등산로 길이

    # 탐색 시작
    for start_node in s:
        recur([start_node], 1, visited, 1)
        # print()

    print(f'#{t}', max_cnt)

    # 상태트리 -> DFS/백트래킹 - 재귀/반복문
    # 스택을 사용하면 visited 때문에 가지치기가 제대로 되지 않음
    # 또한 visited 로 거리를 누적하려고 해도 다른 경로랑 겹쳐서 정확하게 나오지 않음
    # while s:
    #     x, y = s.pop()
    #     current_node = mat[x][y] # 현재 높이
    #     print((x, y), current_node)
    #
    #     if not visited[x][y]: # 방문한적이 없으면
    #         visited[x][y] = 1 # 방문 표시
    #
    #         for dx, dy in delta:
    #             nx, ny = x+dx, y+dy # 다음 좌표 계산
    #
    #             if not (0<=nx<N and 0<=ny<N): # 범위 벗어나면, 다음 방향 탐색
    #                 continue
    #
    #             if visited[nx][ny] : # 방문한 적 있으면, 다음 방향 탐색
    #                 continue
    #
    #             next_node = mat[nx][ny] # 다음 높이
    #
    #             # 현재 높이 미만일때, 바로 stack 에 추가
    #             if current_node > next_node:
    #                 s.append((nx, ny))
    #                 print((nx, ny), mat[nx][ny])
    #
    #             # 현재 높이 이상일때, 차가 K보다 작고 깍을 횟수가 남아있다면, 깎은 후 추가
    #             elif next_node - current_node <= K and chance :
    #                 chance -= 1
    #                 mat[nx][ny] = current_node - 1
    #                 s.append((nx, ny))
    #                 print((nx, ny), mat[nx][ny], chance)