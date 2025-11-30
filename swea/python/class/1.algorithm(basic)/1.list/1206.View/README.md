# ⭐기준점을 중심으로 양옆을 순회한다⭐

### max() 구현

```python
    sum = 0 
    
    # 주변 빌딩 4개 구하기
    for i in range(2, N-2) : 
        side_list = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]] 

        # 주변 빌딩 높이 중 최댓값 구하기
        max_side = side_list[0] 
        for side in side_list :             
            if max_side < side :
                max_side = side

        # 주변 빌딩중 가장 높은 것과의 차이가 전망권
        if max_side < arr[i] :
            sum += (arr[i] - max_side)
```

---

### Delta 구현

```python
    # 기준점(i)은 [2]부터 [N-2] 까지 이동
    # 비교점(j)는 기준점으로부터 양옆으로 2칸씩
    # 비교점 중 가장 큰 값과 기준점을 비교하여, 기준점보다는 작지만 차가 존재할때, 전망권 누적

    # 델타..?
    # 기준점(i)는 모든 칸 이동
    # 비교점(j)는 기준점으로부터 양옆으로 2칸씩
    # 비교점 중 가장 큰 값과 기준점을 비교하여, 기준점보다는 작지만 차가 존재할때, 전망권 누적

    count = 2 # 얖옆으로 2칸씩
    delta = [-1, 1] # 방향벡터 리스트
    sum = 0 # 전망권 누적

    for i in range(N) : # 기준점 이동
        here = arr[i]   # 기준점 높이

        # 주변 건물 중 최댓값 구하기
        max_side = 0
        for di in delta : # 방향벡터 꺼내기

            for c in range(1, count+1) : # 곱해서 0이 되면 안되므로 1부터 시작한다
                ni = i + di * c

                # 범위 안에 있을때,
                # 최댓값보다 크면 최댓값 갱신
                if 0<=ni<N and max_side<arr[ni]:
                    max_side = arr[ni]

        # 기준점 높이보다 작으면, 차를 누적하기
        if here > max_side :
            sum += (here - max_side)

    print(sum)

```