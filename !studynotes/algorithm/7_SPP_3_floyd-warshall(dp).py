'''
- 모든 정점 쌍 사이의 최단 거리 구하기
- 음의 가중치 가능
- 동적프로그래밍(DP)
'''
'''
플로이드 워셜은 O(V^3)이어서, 파이썬으로 하면 시간초과 걸린다 (거의 불가능)
'''

import sys
sys.stdin = open('input.txt')

INF = float('inf') # 최댓값 설정 : 직접 손으로 구해서 넣는 방법도 좋음

# 입력 ----------------------------------------------------------------

V, E = map(int, input().split())

adj_mat = [[INF] * (V+1) for _ in range(V+1)] # 인접행렬
for i in range(1, V+1): # 대각선(자기 자신)은 0
    adj_mat[i][i] = 0
for _ in range(E):
    n1, n2, w = map(int, input().split())
    # adj_mat[n1][n2] = min(adj_mat[n1][n2], w)
    if w < adj_mat[n1][n2]: # 중복 간선 최솟값 유지
        adj_mat[n1][n2] = w # 단방향 (필요시 양방향이면 대칭적으로 값을 설정)


# 함수 ----------------------------------------------------------------

def floyd_warshall():
    distances = [row[:] for row in adj_mat] # 깊은 복사

    for k in range(1, V+1):
        for x in range(1, V+1):
            for y in range(1, V+1):
                # INF + 값 = INF 이긴 하지만, 불필요한 연산 줄이기
                if distances[x][k] == INF or distances[k][y] == INF:
                    continue
                # 거쳐가는 경로가 더 짧으면 업데이트
                if distances[x][k] + distances[k][y] < distances[x][y]:
                    distances[x][j] = distances[x][k] + distances[k][y]

    return distances

# 코드 ----------------------------------------------------------------

dist = floyd_warshall()
has_neg_cycle = any(dist[i][i] < 0 for i in range(1, V + 1))
if has_neg_cycle:
    print("NEGATIVE CYCLE")
else:
    for i in range(1, V + 1):
        row_out = []
        for j in range(1, V + 1):
            row_out.append("INF" if dist[i][j] == INF else str(dist[i][j]))
        print(' '.join(row_out))
