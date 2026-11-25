## 내 코드

- 첫번째 원소 기준으로 "내림차순"
- 두번째 원소 기준으로 "오름차순"

```python
   arr.sort(key=lambda x : (-x[0], x[1]))
```

<hr>

## 시간 복잡도

- 외부 루프 : O(N)
- count() 함수 : O(M)
- 내부 루프 : O(M)
- 총 시간 복잡도 : O(N*M)

<hr>

# ⭐ Counter 모듈 사용방법 ⭐

```python
from collections import Counter

# 리스트의 항목 개수 세기
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(data)

print(counter)  # 출력: Counter({4: 4, 3: 3, 2: 2, 1: 1})
```

```python
from collections import Counter

# 문자열에서 각 문자 개수 세기
text = "hello world"
counter = Counter(text)

print(counter)  # 출력: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

```python
from collections import Counter

data = ['a', 'b', 'c', 'a', 'b', 'a', 'a']
counter = Counter(data)

# 가장 많이 등장한 항목 2개
print(counter.most_common(2))  # 출력: [('a', 4), ('b', 2)]
```

```python
from collections import Counter

counter1 = Counter(a=3, b=2)
counter2 = Counter(a=1, b=4, c=2)

# 두 Counter 합치기
print(counter1 + counter2)  # 출력: Counter({'a': 4, 'b': 6, 'c': 2})

# 두 Counter 빼기
print(counter1 - counter2)  # 출력: Counter({'a': 2, 'b': -2})
```

```python
from collections import Counter

data = ['a', 'b', 'b', 'c', 'c', 'c']
counter = Counter(data)

# 각 항목을 등장 횟수만큼 반환
print(list(counter.elements()))  # 출력: ['a', 'b', 'b', 'c', 'c', 'c']
```

```python
from collections import Counter

counter = Counter(a=2, b=3)

# 새로운 데이터로 카운터 업데이트
counter.update(['a', 'b', 'c', 'c', 'd'])
print(counter)  # 출력: Counter({'b': 4, 'a': 3, 'c': 2, 'd': 1})

```
