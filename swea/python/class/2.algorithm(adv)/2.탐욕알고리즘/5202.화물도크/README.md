# ⭐key=lambda x: (x[0], -x[1])⭐

### ✅ 람다식 활용해서 x 기준으로 / y 기준으로 정렬하기

```python
my_list = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 2)]

# sorted() 함수를 사용하여 정렬
sorted_list = sorted(my_list, key=lambda x: (x[0], -x[1]))
print(sorted_list) # 결과: [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 2)]

# 원본 리스트를 sort() 메서드로 정렬
my_list.sort(key=lambda x: (x[0], -x[1]))
print(my_list) # 결과: [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 2)]
```