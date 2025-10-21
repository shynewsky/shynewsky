import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

# 함수 --------------------------------------------------------------

def prim(start_node):
    global min_weight

    pq = [(0, start_node)] # (가중치, 현재노드)
    visited = [0] * (V+1)

    while pq:
        current_weight, current_node = heappop(pq)

        if visited[current_node]:
            continue

        visited[current_node] = 1 # 최소비용이 되게 하려면 여기서 방문처리를 해야한다
        min_weight += current_weight # 누적합 추가

        for next_node in range(V+1):
            if adj_mat[current_node][next_node] != 0 and visited[next_node] == 0:
                # visited[current_node] = 1 # 여기서 방문처리 하면 최소 비용 후보가 사라진다
                heappush(pq, (adj_mat[current_node][next_node], next_node))

    return

# 입력 --------------------------------------------------------------

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    adj_mat = [[0] * (V+1) for _ in range(V+1)] # 인접행렬
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_mat[n1][n2] = w
        adj_mat[n2][n1] = w

    # 코드 --------------------------------------------------------------

    min_weight = 0 # 가중치의 합
    start_node = 0
    prim(start_node)

    # 출력 --------------------------------------------------------------

    print(f'#{t}', min_weight)
