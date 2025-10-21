'''
- 시작정점에서 모든정점으로의 최단거리 구하기
- 음의 가중치 가능
- 동적프로그래밍(DP)
'''

import sys
sys.stdin = open('input.txt')

INF = float('inf') # 최댓값 설정 : 직접 손으로 구해서 넣는 방법도 좋음

# 입력 ----------------------------------------------------------------

V, E = map(int, input().split())

edge_list = [] # 인접리스트 말고, 간선리스트 사용
for _ in range(E):
    n1, n2, w = map(int, input().split())
    edge_list.append((n1, n2, w))

# 함수 ----------------------------------------------------------------

def bellman_ford(start_node):
    distances = [INF] * (V+1)
    distances[start_node] = 0

    for _ in range(V-1):
        updated = False
        for n1, n2, w in edge_list:
            # start_node 만 0인 상태 ㅡ> 시작노드부터, 누적된 거리를 등록
            if distances[n1] != INF and distances[n2] > distances[n1] + w:
                distances[n2] = distances[n1] + w
                updated = True
        if not updated:
            break

    for n1, n2, w in edge_list:  # 음의 사이클 체크: 한 번 더 확인
        if distances[n1] != INF and distances[n2] > distances[n1] + w:
            return None         # 음의 사이클 존재

    return distances

# 코드 ----------------------------------------------------------------

start_node = 1
result = bellman_ford(start_node)
if result is None:
    print("NEGATIVE CYCLE")
else:
    for v in range(1, V + 1):
        print(result[v] if result[v] != INF else "INF")
