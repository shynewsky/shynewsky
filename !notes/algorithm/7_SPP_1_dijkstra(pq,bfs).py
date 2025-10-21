'''
- 시작정점에서 모든정점으로의 최단거리 구하기
- 음의 가중치 불가능
- 우선순위 큐 사용
'''

import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush
INF = float('inf') # 최댓값 설정 : 직접 손으로 구해서 넣는 방법도 좋음

# 입력 ----------------------------------------------------------------

V, E = map(int, input().split())

adj_list = [[0] for _ in range(V)] # 인접리스트 - [과제] 인접행렬
for _ in range(E):
    n1, n2, w = map(int, input().split())
    adj_list[n1].append((w, n2)) # (주의) 단방향

# 함수 ----------------------------------------------------------------

def dijkstra(start_node):
    pq = [(0, start_node)] # (누적거리, 노드번호)
    distances = [INF] * (V+1)  # 각 정점까지의 최단거리를 저장하는 리스트
    distances[start_node] = 0  # 시작노드 최단거리는 0

    while pq:
        current_dist, current_node = heappop(pq)

        if distances[current_node] < current_dist: # 더 작은값으로 온 적이 있으면 버린다 - (3,c), (4,c)
            continue

        for next_dist, next_node in adj_list[current_node]:
            new_dist = current_dist + next_dist # 누적거리 = 현재까지의 거리 + 다음 거리
            
            if distances[next_node] <= new_dist: # 이미 같거나 작은 가중치로 온 적이 있다면 버린다
                continue

            distances[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return distances

# 코드 ----------------------------------------------------------------

start_node = 1
result = dijkstra(start_node)
print(result)

