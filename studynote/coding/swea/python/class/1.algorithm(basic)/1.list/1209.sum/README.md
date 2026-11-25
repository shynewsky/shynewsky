# 리스트 슬라이싱, ⭐zip()으로 열의 합을 구할 수 있다⭐


### 리스트 컴프리헨션

- zip() 으로 열의 합을 구할 수 있다 ㅡ zip(*matrix) 는 자기자신끼리 zip 하는 것, zip(m1, m2) 는 두개를 zip 하는 것

```python
import sys
sys.stdin = open('input.txt')

T = 10 # 테스트 케이스 수

for _ in range(1, T+1):

    # 입력
    test_case = int(input())
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 변수
    sum_list = []

    # 행의 합을 한꺼번에 계산
    sum_list.extend([sum(row) for row in matrix])

    # 열의 합을 한꺼번에 계산 - zip() 활용
    sum_list.extend([sum(col) for col in zip(*matrix)])

    # 대각선의 합을 구하여 하나씩 추가
    diagonal1 = sum(matrix[i][i] for i in range(N))
    diagonal2 = sum(matrix[i][N - 1 - i] for i in range(N))
    sum_list.append(diagonal1)
    sum_list.append(diagonal2)

    # 출력
    print(f'#{test_case} {max(sum_list)}')
```

---

### 리스트 슬라이싱

- 행의 합은 1중 for 문으로 가능하고
- 열의 합은 2중 for 문으로 가능하다

```python
import sys
sys.stdin = open('input.txt')

T = 10 # 테스트 케이스 수

for _ in range(1, T+1):

    # 입력
    test_case = int(input()) # 테스트 케이스 번호
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)] # 100*100

    sum_list = []
    diagonal1 = 0
    diagonal2 = 0

    for i in range(N):
        # 행 합 구하기
        sum_list.append(sum(matrix[i]))

        # 열 함 구하기
        sum_column = 0
        for j in range(N):
            sum_column += matrix[j][i]
        sum_list.append(sum_column)

        # 대각선 합 구하기
        diagonal1 += matrix[i][i]
        diagonal2 += matrix[i][N-1-i]

    sum_list.append(diagonal1)
    sum_list.append(diagonal2)

    print(max(sum_list))
```

---

### 첫 코드

```python
T = 10 # 테스트 케이스 수

for _ in range(1, T+1):

    # 입력
    test_case = int(input()) # 테스트 케이스 번호
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)] # 100*100

    sum_list = []
    diagonal1 = 0
    diagonal2 = 0

    for i in range(N):
        # 행 합 구하기
        sum_list.append(sum(matrix[i]))

        # 열 함 구하기
        sum_column = 0
        for j in range(N):
            sum_column += matrix[j][i]
        sum_list.append(sum_column)

        # 대각선 합 구하기
        diagonal1 += matrix[i][i]
        diagonal2 += matrix[i][N-1-i]

    sum_list.append(diagonal1)
    sum_list.append(diagonal2)

    print(f'#{test_case} {max(sum_list)}')
```
