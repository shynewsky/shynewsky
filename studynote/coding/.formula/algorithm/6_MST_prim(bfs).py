'''
- heapq 활용한 BFS 사용
- 인접리스트/인접행렬 생성
'''

from heapq import heappop, heappush

# 입력 --------------------------------------------------------------

V, E = map(int, input().split())

adj_mat = [[0] * (V+1) for _ in range(V+1)] # 인접행렬
for _ in range(E):
    n1, n2, w = map(int, input().split())
    adj_mat[n1][n2] = w
    adj_mat[n2][n1] = w

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

# 코드 --------------------------------------------------------------

min_weight = 0 # 가중치의 합
start_node = 0
prim(start_node)

# 출력 --------------------------------------------------------------

print(min_weight)
