'''
플로이드 워셜은 O(V^3)이어서
파이썬으로 하면 웬만하면 시간초과 걸린다
'''

import sys
sys.stdin = open('input.txt')
INF = float('inf')

# 함수 ------------------------------------------------------------

def floyd_warshall():
    distances = [row[:] for row in adj_mat] # 행렬전체 깊은복사

    for k in range(V+1): # 경유지 후보
        for x in range(V+1): # 행 순회
            for y in range(V+1): # 열 순회
                if distances[x][y] > distances[x][k] + distances[k][y]:
                    distances[x][y] = distances[x][k] + distances[k][y]

    return distances

# 입력 ----------------------------------------------

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split()) # 0~V 노드번호, E 간선개수

    # 인접행렬
    adj_mat = [[INF] * (V+1) for _ in range(V+1)] # V+1 노드개수
    for i in range(V+1):   # 대각선(자기 자신)은 0
        adj_mat[i][i] = 0
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        # 중복간선 최솟값 유지
        adj_mat[n1][n2] = min(adj_mat[n1][n2], w) # 단방향

    # 변수/출력
    start_node, end_node = 0, V
    result = floyd_warshall()
    answer = result[start_node][end_node]
    print(f'#{t}', 'inf' if answer == INF else answer)
