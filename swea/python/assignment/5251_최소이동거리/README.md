# *️⃣ 인접리스트

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

# *️⃣ 인접행렬

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

# *️⃣ 인접딕셔너리

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