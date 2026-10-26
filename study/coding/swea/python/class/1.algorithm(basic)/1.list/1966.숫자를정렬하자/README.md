# 입출력, 버블정렬, 카운팅정렬, 선택정렬

### 행 / 행렬 입력받는 방법

```python
    # 행 받는 방법
    array = list(map(int, input().split()))
```
```python
    # 행렬받는 방법
    matrix = [list(map(int, input().split())) for _ in range(N)]
```

---

### 버블 정렬

```python
    # 범위(i)는 뒤에서부터 줄어들고
    # 기준값(j)는 앞에서부터 이동한다

    for i in range(N-1, 0, -1) : # i 로 범위를 뒤에서부터 좁혀온다
        for j in range(0, i) :   # i 는 뒷쪽 범위를 뜻한다
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
```

---

### 카운팅 정렬

```python
    # array 의 값이 counts 의 인덱스가 되고
    # counts 의 값이 temps 의 인덱스가 된다

    # 1. array 에서 각 항목들의 발생횟수를 세고, 정수를 인덱스로 하는 counts 에 저장한다
    max_num = max(array)           # 최댓값을 구한다
    counts = [0] * (max_num + 1)   # 최댓값보다 1 큰 크기의 배열을 만든다
    for i in range(N) :            # array 순회
        counts[array[i]] += 1      # counts 배열 채우기

    # 2. 정렬된 집합에서 각 항목의 앞에 위치할 개수를 반영하기 위해 counts 의 원소를 조정한다
    # counts_before = [1, 3, 1, 1, 2]
    # counts_after = [1, 4, 5, 6, 8] 로 누적합 배열로 만든다
    for i in range(1, max_num + 1) :
        counts[i] += counts[i - 1]

    # 3. array 를 역순으로 순회하면서, counts 를 감소시키고, temp 에 삽입한다
    temps = [0] * N                 # array 랑 같은 크기의 배열 만들기
    for i in range(N-1, -1, -1) :   # array 를 역순으로 순회하면서
        counts[array[i]] -= 1               # count 에서 1을 감소시키고
        temps[counts[array[i]]] = array[i]  # temp 에 array 값을 넣는다
```

---

### 선택 정렬

```python
    # 범위(i)는 앞에서부터 줄어들고
    # '인덱스'로 '최솟값' 을 구하고
    # 두번째값(j)는 끝(N)까지 순회한다

    for i in range(N-1):

        min_idx = i                   # 가장 첫 인덱스를 최소값의 인덱스라고 설정하고
        for j in range(i+1, N):       # 범위의 두번째 인덱스부터 순회하며
            if array[min_idx ] > array[j] :  # 최솟값인지 확인하고,
                min_idx = j           # 최소값을 구하는게 아니라, 최솟값의 인덱스를 구한다

        array[i], array[min_idx] = array[min_idx], array[i]  # 첫 값과, 찐 최소값 자리를 교환한다
```

---

### 출력 방법

```python
    print(f'#{test_case}', end='')
    for i in range(N) :
        print(f' {array[i]}', end='')

    if test_case != T :
        print()
```
