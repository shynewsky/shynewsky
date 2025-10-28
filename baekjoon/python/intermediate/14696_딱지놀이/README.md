### ⭐입력 나눠 받는 방법

```python
a, *A = list(map(int, input().split()))
b, *B = list(map(int, input().split()))

# 4 3 3 2 1
# 4개 [3, 3, 2 1]
```

### ⭐count 배열 생성 후, 역순으로 돌기 (ㅎㄱㅇ님)

```python
    A_list = [0] * 5
    B_list = [0] * 5

    for i in A[1:]:
        A_list[i] += 1
    for j in B[1:]:
        B_list[j] += 1

    result = 'D'

    for i in range(4, 0, -1):
        if A_list[i] > B_list[i]:
            result = 'A'
            break
        elif A_list[i] < B_list[i]:
            result = 'B'
            break

    print(result)
```
