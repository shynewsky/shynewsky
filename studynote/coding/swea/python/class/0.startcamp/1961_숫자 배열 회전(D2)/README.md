## 학습 포인트 - 문자열, 깊은 복사😭

```python
#copy.deepcopy()를 사용한 깊은 복사
import copy
temp_matrix = copy.deepcopy(matrix)

#리스트 컴프리센현으로 직접 복사
temp_matrix = [row[:] for row in matrix]
```
```python
#join() : 문자열을 합치는 메소드
'구분자'.join(반복가능한_문자열들)

for i in range(3):  # 각 행 인덱스
    row1 = ''.join(map(str, mat1[i]))
    row2 = ''.join(map(str, mat2[i]))
    row3 = ''.join(map(str, mat3[i]))
    print(row1, row2, row3)
```
```python
#행렬만들기 
#행을 먼저 받은 후, 행을 쌓아서 열을 만든다

N = int(input()) #행/열 개수
matrix = list() #빈 행렬 선언

for _ in range(0, N) : #열 개수 만큼 반복
    row = list(map(int, input().split())) #행 원소 입력
    matrix.append(row)
```

## 가장 짧은 코드

```python
for j in range(int(input())):
    n = range(int(input()))
    m = list(reversed(n))
    N=[[int(x) for x in input().split()] for _ in n]
    a = [[N[x][y]for x in m]for y in n]
    b = [[a[x][y]for x in m]for y in n]
    c = [[b[x][y]for x in m]for y in n]
    print(f"#{j+1}")
    for i in n:
        print(*a[i]," ",*b[i]," ",*c[i]," ",sep="")
```

