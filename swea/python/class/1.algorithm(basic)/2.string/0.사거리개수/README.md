# Delta

```python
N = int(input())  # 행/열 수
matrix = [list(input()) for _ in range(N)]
# 문자열도 문자 배열이므로, 내부 동작은 일반 배열과 같다.
# list(문자열) 은 그저 '' 로 묶인 문자배열을 [] 로 바꿔 보여주는 것과 같다 (내부동작 구조를 들어내는 느낌)
```

```python
# 델타
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

total_count = 0 # 사거리 개수

for i in range(N):  # 기준점 행 이동
    for j in range(N):  # 기준점 열 이동

        count = 0 # 거리 개수 초기화

        for di, dj in delta : # 방향벡터 꺼내기
            ni, nj = i + di, j + dj # 주변 칸 검색

            # 전체행렬 범위에서 벗어나지 않을때,
            # 1 이 아닐때
            # 1(정수)가 아니라 '1'(문자열)로 비교해야함 ㅡㅡ 저번에도 틀렸던 부분
            if 0<=ni<N and 0<=nj<N and matrix[i][j] != '1' and matrix[ni][nj] != '1' :
                count += 1

        if count == 4 :
            total_count

```