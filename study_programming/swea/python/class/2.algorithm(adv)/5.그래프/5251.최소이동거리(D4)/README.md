# Dijkstra (인접리스트, 인접행렬, 인접딕셔너리), Bellman-Ford, Floyd-Warshall

## Dijkstra

### *️⃣ 인접리스트

- 변수 선언
```python
    # 인접리스트 [[(1, 1), (6, 2)], [(1, 2)], []]
    adj_list = [[] for _ in range(V+1)] # V+1 노드개수
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_list[n1].append((w, n2))
```
- 다음 노드 검색
```python
    for next_dist, next_node in adj_list[current_node]: # 다음 노드 순회
        new_dist = current_dist + next_dist # 누적거리 = 현재까지 누적거리 + 다음거리
```
<hr>

### *️⃣ 인접행렬

- 변수 선언
```python
    # 인접행렬 [[0, 1, 6], [0, 0, 1], [0, 0, 0]]
    # 0으로 초기화하면, 시작노드의 가중치와 겹치기 때문에 INF로 초기화한다
    adj_mat = [[INF] * (V+1) for _ in range(V+1)] # V+1 노드개수
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_mat[n1][n2] = w # 단방향
```
- 다음 노드 검색

```python
    for next_node in range(V+1): # 다음 노드 순회
        next_dist = adj_mat[current_node][next_node]
        new_dist = current_dist + next_dist # 누적거리 = 현재까지 누적거리 + 다음거리
```

<hr>

### *️⃣ 인접딕셔너리

- 변수 선언

```python
    # 인접딕셔너리 {0: [(1, 1), (6, 2)], 1: [(1, 2)], 2: []}
    adj_dict = {i : [] for i in range(V+1)} # V+1 노드개수
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_dict[n1].append((w, n2)) # 단방향
```
- 다음 노드 검색
```python
    for next_dist, next_node in adj_dict[current_node]: # 다음 노드 순회
        new_dist = current_dist + next_dist # 누적거리 = 현재까지 누적거리 + 다음거리
```

---

## Bellman-Ford

```python
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
```

---

## Floyd-Warshall

```python
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
```