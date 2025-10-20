import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush
INF = int(21e8) # 최댓값 설정 : 직접 손으로 구해서 넣는 방법도 좋음

# 입력 ----------------------------------------------------------------

V, E = map(int, input().split())

adj_list = [[0] for _ in range(V)] # 인접리스트 - [과제] 인접행렬
for _ in range(E):
    n1, n2, w = map(int, input().split())
    adj_list[n1].append((w, n2)) # (주의) 단방향

# 함수 ----------------------------------------------------------------

def dijkstra(start_node):
    pq = [(0, start_node)] # (누적거리, 노드번호)
    dists = [INF] * V      # 각 정점까지의 최단거리를 저장하는 리스트
    dists[start_node] = 0  # 시작노드 최단거리는 0

    while pq:
        distance, current_node = heappop(pq)

        if dists[current_node] < distance: # 더 작은값으로 온 적이 있으면 버린다 - (3,c), (4,c)
            continue

        for next_distance, next_node in adj_list[current_node]:
            new_distance = distance + next_distance # 누적거리 = 현재까지의 거리 + 다음 거리
            
            if dists[next_node] <= new_distance: # 이미 같거나 작은 가중치로 온 적이 있다면 버린다
                continue

            dists[next_node] = new_distance
            heappush(pq, (new_distance, next_node))

    return dists

# 코드 ----------------------------------------------------------------

start_node = 0
result = dijkstra(start_node)
print(result)

