'''
- 시작정점에서 모든정점으로의 최단거리 구하기
- 음의 가중치 가능
- 동적프로그래밍(DP)

- 간선리스트 사용(인접리스트 아님)
'''

import sys
sys.stdin = open('input.txt')
INF = float('inf')

# 함수 ------------------------------------------------------------

def bellman_ford(start_node):
    distances = [INF] * (V+1)
    distances[start_node] = 0

    # V-1 대신 E 를 쓰면 안되는 이유
    # "최대 V-1개 간선을 거쳐야 최단 경로가 완성된다"
    for _ in range(V-1):
        updated = False
        for n1, n2, w in edges:
            # distance 에 기록되어있고, 기존 기록보다 짧으면 기록/갱신
            if distances[n1] != INF and distances[n2] > distances[n1] + w:
                distances[n2] = distances[n1] + w
                updated = True
        if not updated:
            break

    for n1, n2, w in edges:
        # 누적거리에서 기존 기록보다 짧아지는 구간이 있으면, 음의 사이클 존재
        if distances[n1] != INF and distances[n2] > distances[n1] + w:
            return None # 음의 사이클 존재

    return distances

# 입력 ----------------------------------------------

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split()) # 0~V 노드번호, E 간선개수

    # 간선리스트 [(0, 1, 1), (0, 2, 6), (1, 2, 1)]
    edges = []
    for _ in range(E):
        edges.append(tuple(map(int, input().split())))

    # 변수/출력
    start_node, end_node = 0, V
    result = bellman_ford(start_node)
    print(f'#{t}', result[end_node])
