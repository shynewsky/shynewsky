'''
- 시작정점에서 모든정점으로의 최단거리 구하기
- 음의 가중치 불가능
- 우선순위 큐 사용
'''

import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush
INF = float('inf')

# 함수 ------------------------------------------------------------

def dijkstra(start_node):

    # 우선순위큐 : 일반 리스트로 만들되, heappop/heappush 함수 사용
    pq = [(0, start_node)] # (누적거리, 노드번호)

    # distance : 해당 정점까지의 최단 누적거리 리스트 (pq에 넣는 동시에 기록)
    distances = [INF] * (V+1) # V+1 노드개수
    distances[start_node] = 0 # 시작노드까지의 최단누적거리는 0

    while pq:
        current_dist, current_node = heappop(pq)

        # 이미 더 작은 값으로 온 적이 있으면 무시 (누적거리 계산하지 않을 것이다)
        if distances[current_node] < current_dist:
            continue

        for next_dist, next_node in adj_dict[current_node]: # 다음 노드 순회
            new_dist = current_dist + next_dist # 누적거리 = 현재까지 누적거리 + 다음거리

            # 이미 더 작거나 같은 값으로 온 적이 있으면 무시 (pq에 넣지 않을 것이다)
            if distances[next_node] <= new_dist:
                continue

            heappush(pq, (new_dist, next_node)) # (누적거리, 다음노드)를 pq에 올린다
            distances[next_node] = new_dist     # pq에 올리는 동시에 (누적거리) 기록

    return distances # [0, 1, 2]

# 입력 ----------------------------------------------

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split()) # 0~V 노드번호, E 간선개수

    # 인접딕셔너리 {0: [(1, 1), (6, 2)], 1: [(1, 2)], 2: []}
    adj_dict = {i : [] for i in range(V+1)} # V+1 노드개수
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_dict[n1].append((w, n2)) # 단방향

    # 변수/출력
    start_node, end_node = 0, V
    result = dijkstra(start_node)
    print(f'#{t}', result[end_node])
