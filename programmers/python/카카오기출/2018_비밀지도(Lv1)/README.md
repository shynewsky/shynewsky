## 1️⃣ 내 코드

```python
def solution(n, arr1, arr2):
    # 10진수를 n자릿수의 2진수로 바꾸는 방법 ==> format(num, f'0{n}b')
    # 근데 2진수끼리 '|' 연산을 하려면 10진수로 바꿔야 한다
    # 자릿수를 맞추지 않아도 10진수끼리 먼저 계산해도 결과는 같으므로, 2진수로 변환하기 전에 먼저 계산한다

    arr3 = []
    for i in range(n):
        arr3.append(format(arr1[i] | arr2[i], f'0{n}b'))

    arr4 = []
    for a in arr3:
        temp = ''
        for b in a:
            temp += '#' if b == '1' else ' '
        arr4.append(temp)

    return arr4
```

## 2️⃣ 시간복잡도 분석

- arr3 : n글자 x n개 = O(n^2)
- arr4 : n글자 x n개 x n줄 = O(n^3)

## 3️⃣ 효율적인 코드

- arr3 을 없애고 join() 또는 translate 를 사용해서 문자열을 한번에 

```python
def solution(n, arr1, arr2):
    out = []
    for i in range(n):
        v = arr1[i] | arr2[i]
        row = ''.join('#' if (v >> (n - 1 - j)) & 1 else ' ' for j in range(n))
        out.append(row)
    return out
```

```python
def solution(n, arr1, arr2):
    trans = str.maketrans({'1': '#', '0': ' '})
    fmt = f'0{n}b'
    return [format(arr1[i] | arr2[i], fmt).translate(trans) for i in range(n)]
```

<hr>

# ⭐ translate() 사용 방법 ⭐

- translate : 문자열의 각 문자을 매핑 테이블에 따라 한번에 치환해주는 내장 메서드
- 이걸 사용하면 for 문으로 문자 하나씩 바꿀 필요 없이, C 레벨에서 빠르게 변환 가능

```python
# 기본구조
table = str.maketrans({'1': '#', '0': ' '})
s = "10110"
print(s.translate(table))
```

```python
# 문제코드 적용
def solution(n, arr1, arr2):
    table = str.maketrans({'1': '#', '0': ' '})
    fmt = f'0{n}b'  # n자리 이진수 포맷
    result = []
    
    for i in range(n):
        merged = arr1[i] | arr2[i]              # 두 배열의 각 원소를 OR 연산
        binary = format(merged, fmt)            # n자리 2진수 문자열
        converted = binary.translate(table)     # '1','0' → '#',' ' 로 치환
        result.append(converted)
    
    return result
```

```python
# 문제코드 적용 & 리스트컴프리헨션
def solution(n, arr1, arr2):
    table = str.maketrans({'1': '#', '0': ' '})
    fmt = f'0{n}b'
    return [format(arr1[i] | arr2[i], fmt).translate(table) for i in range(n)]
```
