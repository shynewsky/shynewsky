## 1️⃣ 내 코드

```python
def solution(dartResult):
    points = [0] * 3
    darts = []
    n = len(dartResult)

    # 문자열 쪼개기
    start, end = 0, 1
    while start < n:
        if dartResult[start].isdigit() and dartResult[end].isdigit():
            end += 1
        else:
            darts.append(dartResult[start:end])
            start = end
            end += 1
            
    # 점수 계산
    idx = -1
    dict = { 'S':1, 'D':2, 'T':3, }
    for dart in darts:
        if dart.isdigit():
            idx += 1
            points[idx] = int(dart)
        if dart in 'SDT':
            points[idx] **= dict[dart]
        if dart == '*':
            if idx == 0:
                points[0] *= 2
            else:
                points[idx-1] *= 2
                points[idx] *= 2
        if dart == '#':
            points[idx] *= -1

    return sum(points)
```

## 2️⃣ 시간복잡도 분석

- 총 O(N)
- 문자열분해 while : O(N)
- 계산 for 루프 : O(1)

## 3️⃣ 효율적인 코드

- 총 O(N)
- 문자열을 쪼개는 동시에 계산 완료해버림
- 시간복잡도는 그대로이지만, 불필요한 슬라이싱/리스트 할당이 사라져 O(1) 이 사라진다

```
ord(N)-48 은 int(N) 와 동일 효과지만, 반복 변환에서 약간 더 직접적입니다.
```
```python
def solution(dartResult):
    points = [] # 각 기회(총 3번)의 점수를 저장할 리스트
    i, n = 0, len(dartResult)

    while i < n:
        num = 0
        while i < n and dartResult[i].isdigit():
            # str(dartResult[i]) 대신 ord('0')==48을 이용한 빠른 정수화.
            num = num * 10 + (ord(dartResult[i]) - 48)
            i += 1

        bonus = dartResult[i]
        i += 1
        if bonus == 'S':
            num **= 1
        elif bonus == 'D':
            num **= 2
        else:  # 'T'
            num **= 3

        if i < n and dartResult[i] in '*#':
            opt = dartResult[i]
            i += 1
            if opt == '*':
                if points:
                    points[-1] *= 2
                num *= 2
            else:  # '#'
                num *= -1

        points.append(num)

    return sum(points)
```

- 정규식 토크나이저

```
tokens = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)

- re.findall(r'(패턴)', 문자열) : 패턴 추출, 튜플 반환, 리스트에 담음
- (/d+) : 숫자
- ([SDT]) : 문자 'SDT' 중 하나
- ([*#]?) : 문자 '*#' 중 하나, 있을수도 없을수도 있음
```
```python
import re

def solution(dartResult: str) -> int:
    tokens = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    pts = []
    powmap = {'S':1, 'D':2, 'T':3}
    
    for a, b, c in tokens:
        x = int(a) ** powmap[b]
        if c == '*':
            if pts:
                pts[-1] *= 2
            x *= 2
        elif c == '#':
            x *= -1
        pts.append(x)
        
    return sum(pts)
```