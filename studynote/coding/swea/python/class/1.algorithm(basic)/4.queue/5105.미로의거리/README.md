# BFS,⭐next((i, j) for i in range(N) for j in range(N) if matrix[i][j] == 2)⭐


### 배운점

- 시작점 찾기 ㅡ next() 안에 튜플 컴프리헨션을 사용한다

```python
    x = y = 0
    for i in range(N): # 기준점 행 이동
        for j in range(N): # 기준점 열 이동
            if matrix[i][j] == 2:
                x, y = i, j
```
```python
    x, y = next((i, j) for i in range(N) for j in range(N) if matrix[i][j] == 2)
```

- visited 를 0으로 초기화하기 떄문에 ㅡ 방문표시는 1로 하는 것이 안전하다

```python
    visited[x][y] = 0
```
```python
    visited[x][y] = 1
```

- visited 를 1로 표시했기 때문에, 개수는 하나 더 빼야한다

```python
            print(f'#{test_case}', visited[x][y] -1)
```
```python
            print(f'#{test_case}', visited[x][y] -2)
```

- visited 로 방문표시를 하기 때문에, matrix[i][j] = 2 를 할 필요가 없다

```python
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0 :
                if matrix[nx][ny] == 0 or matrix[nx][ny] == 3:
                    matrix[x][y] = 2
```
```python
            if 0<=nx<N and 0<=ny<N and matrix[nx][ny] != 1 and visited[nx][ny] == 0 :
```