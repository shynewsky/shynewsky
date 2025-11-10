## 1️⃣ 내 코드

- 총 시간복잡도 : O(N^2)


- for문 : O(N)
- arr.pop(i) : O(N)

```python
def solution(arr):
    N = len(arr)
    for i in range(N-1, 0, -1):
        if arr[i] == arr[i-1]:
            arr.pop(i)
    return arr
```
---
## 2️⃣ 효율적인 코드

```python
from itertools import groupby

def solution(arr):
    return [k for k, _ in groupby(arr)]
```

### ⭐ itertools.groupby

- <ins>**연속된 값끼리 묶어주는 함수**</ins>
- 정렬되어있지 않더라도, 중복이 떨어져있으면 다른 그룹으로 나뉨

```python
groupby(iterable, key=None)
```
- iterable을 순서대로 읽으면서,
- 키 값이 동일하게 연속되는 요소들을 묶어서
- (key, group_iterator) 쌍으로 반환한다

```python
from itertools import groupby

result = [k for k, _ in groupby(data)]

# data = [1, 1, 2, 2, 2, 3, 1, 1]
# result = [1, 2, 3, 1]
```
```python
from itertools import groupby

result = [k for k, _ in groupby(data)]

# data = [1, 2, 1, 2, 1, 2]
# result = [1, 2, 1, 2, 1, 2]
```
- key 함수 사용 : 대소문자 무시하고 그룹화
```python
from itertools import groupby

for key, group in groupby(data, key=str.lower):
    print(key, list(group))

# data = "AAaaBBbCCC"
# a ['A', 'A', 'a', 'a']
# b ['B', 'B', 'b']
# c ['C', 'C', 'C']
```
