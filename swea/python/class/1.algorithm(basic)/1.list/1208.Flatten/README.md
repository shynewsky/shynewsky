### 내장함수 사용

```python
    # 평탄화 할 방법
    # 가장 높은 곳을 찾아서 -1 하고, 가장 낮을 곳을 찾아서 +1 한다
    for i in range(N) :
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
```

---

### max()로 구현

```python
    # 평탄화 할 방법
    # 가장 높은 곳을 찾아서 -1 하고, 가장 낮을 곳을 찾아서 +1 한다

    # 덤프 수행
    for i in range(N) :

        # 최댓값, 최솟값 구하고
        # 최댓값, 최소값 인덱스 구하기
        # range() 에는 N 말고 100 넣어야 함
        max_num, min_num = arr[0], arr[0]
        max_idx, min_idx = 0, 0
        for i in range(100):
            if max_num < arr[i]:
                max_num = arr[i]
                max_idx = i
            if min_num > arr[i]:
                min_num = arr[i]
                min_idx = i

        if max_num - min_num <= 1:
            break

        # 최댓값에서 1 빼고, 최솟값에서 1 더해야한다
        arr[max_idx] -= 1
        arr[min_idx] += 1

    # 덤프가 끝난 후의 최댓값과 최솟값 구하기
    max_val, min_val = arr[0], arr[0]
    for i in range(100):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]
```