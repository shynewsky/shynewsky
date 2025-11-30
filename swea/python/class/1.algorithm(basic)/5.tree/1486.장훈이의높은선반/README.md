# DP

### 1. 백트래킹 - path (제한시간초과 8/10)

```python
import sys
sys.stdin = open('input.txt')

def recur(n):
    global min_sum

    if min_sum < sum(path): # 가지치기
        return

    if sum(path) >= B: # 종료조건
        if min_sum > sum(path):
            min_sum = sum(path)
        return

    for i in range(N): # arr 순회
        if visited[i] == 1:
            continue
        visited[i] = 1
        path.append(arr[i])
        recur(n+1)
        path.pop()
        visited[i] = 0

T = int(input())
for t in range(1, T+1):
    # 입력
    N, B = map(int, input().split()) # N명, B높이
    arr = list(map(int, input().split())) # N명
    # 변수
    path = []
    visited = [0] * N
    min_sum = float('inf')
    # 풀이
    recur(0)
    # 출력
    print(f'#{t}', min_sum-B)
```

---

### 2. 백트래킹 - sum (제한시간초과 8/10)

```python
import sys
sys.stdin = open('input.txt')

def recur(n, s):
    global min_sum

    if min_sum < s: # 가지치기
        return

    if s >= B: # 종료조건
        if min_sum > s:
            min_sum = s
        return

    for i in range(N): # arr 순회
        if visited[i] == 1:
            continue
        visited[i] = 1
        recur(n+1, s+arr[i])
        visited[i] = 0

T = int(input())
for t in range(1, T+1):
    # 입력
    N, B = map(int, input().split()) # N명, B높이
    arr = list(map(int, input().split())) # N명
    # 변수
    visited = [0] * N
    min_sum = float('inf')
    # 풀이
    recur(0,0) # [0]번원소, 합0
    # 출력
    print(f'#{t}', min_sum-B)
```

--- 

### 3. 동적계획법(ButtomUp) 🤖

```python
import sys
sys.stdin = open('input.txt')

def recur():
    global min_sum

    total = sum(arr) # 부분합 표시 테이블(bitset처럼 사용)
    dp = [0] * (total+1)
    dp[0] = 1 # 합0은 항상 가능(아무것도 안고를때)

    for i in range(N): # 각 원소를 한번씩 사용해 부분합 갱신
        for j in range(total-arr[i], -1, -1):
            if dp[j]:
                dp[j+arr[i]] = 1

    for s in range(B, total+1):
        if dp[s]:
            min_sum = s
            return

    return

T = int(input())
for t in range(1, T+1):
    # 입력
    N, B = map(int, input().split()) # N명, B높이
    arr = list(map(int, input().split())) # N명
    # 변수
    min_sum = float('inf')
    # 풀이
    recur()
    # 출력
    print(f'#{t}', min_sum-B)
```