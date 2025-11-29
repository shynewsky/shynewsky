# ✴️ 값 구하기

```python
    # min() ㅡ 최솟값 구하기
    min_num = arr[0]
    for num in arr :
        if min_num > num :
            min_num = num
```

```python
    # max() ㅡ 최댓값 구하기
    max_num = arr[0]
    for num in arr :
        if max_num > num :
            max_num = num
```
# ✴️ 인덱스 구하기

```python
    # min() ㅡ 최솟값 인덱스 구하기
    min_idx = 0
    for idx in range(N) :
        if arr[min_idx] > arr[idx] :
            min_idx = idx
```

```python
    # max() ㅡ 최댓값 인덱스 구하기
    max_idx = 0
    for idx in range(N) :
        if arr[max_idx] > arr[idx] :
            max_idx = idx
```

# ✴️ 마지막 인덱스 구하기 (= 만 붙이면 됨)

```python
    # min() ㅡ 최솟값이 여러개일때, 마지막 인덱스 구하기
    min_idx = 0
    for idx in range(N) :
        if arr[min_idx] >= arr[idx] : # = 하나만 넣어주면 된다
            min_idx = idx
```

```python
    # max() ㅡ 최댓값이 여러개일때, 마지막 인덱스 구하기
    max_idx = 0
    for idx in range(N) :
        if arr[max_idx] >= arr[idx] : # = 하나만 넣어주면 된다
            max_idx = idx
```

# *️⃣ for 문을 합칠 수 있다

```python
    min_num = arr[0]
    max_num = arr[0]

    for num in arr :
        if min_num > num :
            min_num = num
        if max_num > num :
            max_num = num
```
```python
    min_idx = 0
    max_idx = 0

    for idx in range(N) :
        if arr[min_idx] > arr[idx] :
            min_idx = idx
        if arr[max_idx] > arr[idx] :
            max_idx = idx
```

```python
    min_idx = 0
    max_idx = 0

    for idx in range(N) :
        if arr[min_idx] >= arr[idx] :
            min_idx = idx
        if arr[max_idx] >= arr[idx] :
            max_idx = idx
```
