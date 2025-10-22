import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush
INF = float('inf')

'''
- 출발은 항상 (0,0), 도착은 항상 (N-1, N-1)
- 상하좌우 인접지역으로만 이동 가능
- 이동시 기본 1만큼 연료 소모, 높이 차이만큼 추가로 연료 소비

= 시작점 존재, 가중치의 최소합 => SPP(최단경로) 문제
'''

# 함수 ----------------------------------------------------------------------

def dijkstra(start):

    # 우선순위큐 : heappop, heappush 사용
    pq = [(0, start, start)]

    # distance : 해당 정점까지의 최단거리 누적리스트 (pq에 넣는 동시에 기록)
    distances = [[INF] * (N+1) for _ in range(N+1)] # V+1 노드 개수
    distances[start][start] = 0                     # 시작노드까지의 최단누적거리는 0

    while pq :
        current_dist, x, y = heappop(pq)

        # 이미 더 작은 값으로 온 적이 있으면 무시 (누적거리 계산하지 않을 것이다)
        if distances[x][y] < current_dist:
            continue

        for dx, dy in delta: # 다음 노드 순회
            nx, ny = x+dx, y+dy

            if not (0<=nx<N and 0<=ny<N):
                continue

            next_dist = mat[nx][ny]
            new_dist = current_dist + 1
            if mat[nx][ny] > mat[x][y]:
                new_dist += (mat[nx][ny] - mat[x][y])

            # 이미 더 작거나 같은 값으로 온 적이 있으면 무시 (pq에 넣지 않을 것이다)
            if distances[nx][ny] <= new_dist:
                continue

            heappush(pq, (new_dist, nx, ny)) # (누적거리, 다음x좌표, 다음y좌표)
            distances[nx][ny] = new_dist

    return distances

# 입력 -----------------------------------------------------------------------
T = int(input())
for t in range(1, T+1):
    N = int(input()) # N 행/열 수
    mat = [list(map(int, input().split())) for _ in range(N)] # N 지역높이

    # 델타
    delta = ((1,0), (-1,0), (0,1), (0,-1))

    # 변수
    start, end = 0, N-1
    result = dijkstra(start)
    print(f'#{t}', result[end][end])
