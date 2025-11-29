# ⭐list(zip(*matrix[::-1]))⭐
# ⭐[list(row) for row in matrix]⭐

### ✴️ 인덱스 활용

- 시계방향 90도 회전
- 열이 행이 된다
- matrix0[j][N-1-i] = matrix[i][j]

```python
    for i in range(N) : # matrix 행 순회
        for j in range(N) : # matrix 열 순회
            matrix0[j][N-1-i] = matrix[i][j]
```

- 반시계방향 90도 회전
- 행이 열이 된다
- matrix1[N-1-j][i] = matrix[i][j]

```python
    for i in range(N) : # matrix 행 순회
        for j in range(N) : # matrix 열 순회
            matrix1[N-1-j][i] = matrix[i][j]
``` 

<hr>

### ✴️ zip() 활용

- 시계방향 90도 회전
- 행 역순 후 전치 (추천)

```python
    matrix2 = list(zip(*matrix[::-1])) # 행을 역순으로 나열한 후 전치행렬 만들기
    matrix2 = [list(row) for row in matrix2] # 튜플 원소를 리스트 원소로 바꾸기
```

- 반시계방향 90도 회전
- 전치 후 행 역순 (추천)

```python
    matrix4 = list(zip(*matrix))[::-1] # 전치 후 행 역순
    matrix4 = [list(row) for row in matrix4]
```
