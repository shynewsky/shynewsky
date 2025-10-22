import sys
sys.stdin = open('input.txt')

from collections import deque
# BFS
# 그래프 관점에서 “최소 횟수”를 구하는 최단 경로 문제

def bfs(start, target):
    q = deque()
    visited = [0] * (max_val+1)
    visited[start] = 1
    q.append(start)

    while q:
        current_node = q.popleft()

        if current_node == target:
            return visited[current_node]

        next_list = (current_node+1, current_node-1, current_node*2, current_node-10)

        for next_node in next_list:
            if 1<=next_node<=max_val and visited[next_node] == 0:
                visited[next_node] = visited[current_node] + 1
                q.append(next_node)

# 입력 ------------------------------------------------------------------------
T = int(input()) # 테스트케이스
for t in range(1, T+1):
    N, M = map(int, input().split()) # N 시작 자연수, M 자연수 만들기

    # 코드 ---------------------------------------------------------------------
    # min_cnt = float('inf') # n으로 갱신되지 않으면, n을 빼도 'inf'이다
    max_val = 1000000
    min_cnt = bfs(N, M)

    # 출력 ---------------------------------------------------------------------
    print(f'#{t}', min_cnt-1)


# 재귀 = DFS
# 최소 횟수 보장을 위해선 BFS가 정석이다. DFS 해서 기하급수적으로 터지는 것
# def recur(n, sum):
#     global min_cnt
#
#     # 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다
#     if sum > 1000000: # 가지치기
#         return
#
#     if min_cnt <= n: # 가지치기
#         return
#
#     chance = min_cnt - n # 남은 예산
#     if sum * (2 ** chance) < M:
#         return
#
#     if sum - (10 * chance) > M:
#         return
#
#     if sum == M: # 종료조건
#         if min_cnt > n:
#             min_cnt = n
#         return
#
#     recur(n+1, sum+1)
#     recur(n+1, sum-1)
#     recur(n+1, sum*2)
#     recur(n+1, sum-10)
