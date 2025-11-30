# Kruskal, Prim(수업코드)

### ⭐ KRUSKAL

- Union-find 사용
- 간선리스트 생성 (인접리스트 아님)

```python
import sys
sys.stdin = open('input.txt')

# 함수 --------------------------------------------------------------

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union_set(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry: # 같은 집합이면 합치지 않음
        return
    parents[ry] = rx

# 입력 --------------------------------------------------------------

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    edges = [] # 간선리스트
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((n1, n2, w))
    edges.sort(key=lambda x: x[2]) # 가중치 기준으로 오름차순

    # 코드 --------------------------------------------------------------

    parents = [i for i in range(V + 1)]  # make_set()

    cnt = 0 # 선택한 간선의 수
    min_weight = 0 # 가중치의 합

    for n1, n2, w in edges:
        if find_set(n1) != find_set(n2): # 같은 집합이 아니면 연결한다
            union_set(n1, n2)
            cnt += 1
            min_weight += w

            if cnt == V:
                break

    # 출력 --------------------------------------------------------------

    print(f'#{t}', min_weight)
```

---

### ⭐ PRIM

- heapq 활용한 BFS 사용
- 인접리스트/인접행렬 생성

```python
import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

# 함수 --------------------------------------------------------------

def prim(start_node):
    global min_weight

    pq = [(0, start_node)] # (가중치, 현재노드)
    visited = [0] * (V+1)

    while pq:
        current_weight, current_node = heappop(pq)

        if visited[current_node]:
            continue

        visited[current_node] = 1 # 최소비용이 되게 하려면 여기서 방문처리를 해야한다
        min_weight += current_weight # 누적합 추가

        for next_node in range(V+1):
            if adj_mat[current_node][next_node] != 0 and visited[next_node] == 0:
                # visited[current_node] = 1 # 여기서 방문처리 하면 최소 비용 후보가 사라진다
                heappush(pq, (adj_mat[current_node][next_node], next_node))

    return

# 입력 --------------------------------------------------------------

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    adj_mat = [[0] * (V+1) for _ in range(V+1)] # 인접행렬
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_mat[n1][n2] = w
        adj_mat[n2][n1] = w

    # 코드 --------------------------------------------------------------

    min_weight = 0 # 가중치의 합
    start_node = 0
    prim(start_node)

    # 출력 --------------------------------------------------------------

    print(f'#{t}', min_weight)
```