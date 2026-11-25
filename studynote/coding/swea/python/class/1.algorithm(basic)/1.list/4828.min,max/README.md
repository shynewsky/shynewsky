# 같은 작업을 하는 for 문은 하나로 합쳐라

### 값 구하기

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

---

### 인데스 구하기

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

---

### 마지막 인덱스 구하기 (=만 붙이면 됨)

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

---

### for 문을 합칠 수 있다

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

---

### 코드리뷰

```python
    max_num, min_num = arr[0], arr[0]  # 단순 변수 선언은 한 줄로 줄일 수 있다
```
```python
    for i in range(0, N):    # 같은 역할을 하는 for 문은 하나로 합칠 수 있다
        if max_num < arr[i]:
            max_num = arr[i]
        if min_num > arr[i]:
            min_num = arr[i]
```
```python
    for i in range(1, N):   #0번은 이미 넣어놨으니, 1번부터 순회해도 된다
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]
```
```python
    for num in nums:         # 인덱스 대신, 원소 자체로 돌아도 가능하다
        if max_num < num:    
            max_num = num    
        elif min_num > num:   
            min_num = num
```