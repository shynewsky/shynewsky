## 1. 내 코드

- 시간복잡도 : O(N·U^2 + ∑(h_k·w_k))


- 행렬초기화 : o(1)
- 색종이 칠하기 : O(∑(h_k·w_k))
- 개수 세기 : O(N·U^2)

```python
# 53점

# 입력 -------------------------------------------------------
N = int(input()) # 색종이 수 (1<=N<=100)
data = [list(map(int, input().split())) for _ in range(N)]

# 코드 --------------------------------------------------------
'''
평면이 1001 * 1001 = 1천만이 넘어가므로, 1초 넘음. 즉, 최악의 경우 행렬사용불가
'''
mat = [[0] * 1001 for _ in range(1001)]
for n in range(N):
    x, y, h, w = data[n]
    for i in range(x, x+h):
        for j in range(y, y+w):
            mat[i][j] = n+1

for n in range(1, N+1):
    print(sum([row.count(n) for row in mat]))
```

## 2. 다른분 코드

- ChatGPT도 53점 나옴
- 구글링을 통해 다른 분들의 코드를 찾아보았다


- for 문 3개를 `리스트슬라이싱`을 사용하여 2개로 줄일 수 있다
- 입력 받는 동시에 

```python
import sys
input = sys.stdin.readline

N = int(input())
arr = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for j in range(y, y+h):
        arr[j][x:x+w] = [i]*w

for i in range(1, N+1):
    cnt = 0
    for j in range(1001):
        cnt += arr[j].count(i)
    print(cnt)
```