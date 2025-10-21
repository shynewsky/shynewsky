import sys
sys.stdin = open('input.txt')

# 입력 ----------------------------------------------------------------------------
V, E = map(int, input().split())

# 인접행렬
# [과제] 인접리스트로 구현해보기
adj_mat = [[0] * V for _ in range(V)]

for _ in range(E):
    n1, n2, w = map(int, input().split())
    adj_mat[n1][n2] = w
    adj_mat[n2][n1] = w

# 함수 ----------------------------------------------------------------------------

# prim()
# - 특정 정점 기준으로 시작
# - 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 간다
# - 작은 노드를 먼저 꺼내기 위해 우선순위큐(heapq)를 활용한다

#import heapq
from heapq import heappop, heappush

def prim(start_node):
    pq = [(0, start_node)] # (가중치, 노드) 형태 - 앞 원소를 기준으로 정렬되도록
    visited = [0]  * V
    min_weight = 0

    while pq:
        weight, current_node = heappop(pq)

        if visited[current_node] == 0:
            visited[current_node] = 1 # 방문처리
            min_weight += weight

        for next_node in range(V):
            if adj_mat[current_node][next_node] == 1 and visited[next_node] == 0:
                # BFS처럼 여기서 방문처리를 해버리면, 다음에 최소 비용이 들어오면 선택불가 
                heappush(pq, (adj_mat[current_node][next_node], next_node))

    return min_weight

# 코드 ----------------------------------------------------------------------------

result = prim(0) # 출발 정점을 바꾸어도 최소 비용은 똑같다, 단 그래프는 다르게 나올 수 있다
