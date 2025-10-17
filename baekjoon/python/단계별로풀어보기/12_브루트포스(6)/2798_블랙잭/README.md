# ⭐재귀는 O(2^N), 반복문은 O(N^3) 이어서 반복문이 더 낫다⭐

### 1. 직접 설계 ㅡ 32412 KB, 164ms

- N 장의 카드가 주어진다
- 종료조건 : 카드 3개 뽑을때
- 가지치기 : 합이 M 을 넘어갈때

```python
import sys
sys.stdin = open('input.txt')

def recur(n, s):
    global max_sum

    if s > M:
        return

    if n == 3: # 종료조건 ㅡ 카드를 3개 뽑으면 종료
        if max_sum < s and s <= M:
            max_sum = s
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        # path.append(A[i])
        recur(n+1, s+A[i])
        # path.pop()
        visited[i] = 0
    pass

# 입력
N, M = map(int,input().split())
A = list(map(int, input().split()))
# 변수
path = []
visited = [0] * N
max_sum = 0
# 코드
recur(0, 0)
# 출력
print(max_sum)
```

<hr>

### 2. 내 코드 분석

|시간복잡도 ㅡ O(N^3)|공간복잡도 ㅡ O(N)|
|---|---|
| - 깊이가 3 ㅡ P(N,3) = N * (N-1) * (N-2)<br>- 전체 연산 수 ㅡ 최악일때 O(N^3)	| - visited 배열 길이 N ㅡ O(N) <br> - 재귀 깊이 최대 3 ㅡ O(1)<br>- 기타 상수 변수들 ㅡ O(1)|


### 2-1. for문 부분집합 완전탐색

```python
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

mx = 0
for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      s = arr[i]+arr[j]+arr[k]
      if s <= M:
        if mx < s: 
          mx = s
        break

print(mx)
```

### 2-2. Two Pointer 알고리즘

첫 원소를 기준으로, 두번째 원소를 left, 마지막 원소를 right 로 해서

합을 구했을때 M보다 작으면 mx에 저장 후 left 를 올리고, M보다 크면 right 를 내린다

left 와 right 가 교차하면, pivot 을 옮기고 다시 비교하며 진행한다


```python
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

mx = 0
for i in range(N):
    pivot = i
    left = i+1
    right = N-1
    while left < right:
        total = arr[pivot] + arr[left] + arr[right]
        if total <= M:
            if mx < total:
                mx = total
            left += 1
        else:
            right -= 1

print(mx)
```

### 3-1. ㄱㄷㅇ님 (백트래킹 부분집합)

```python
def blackjack(index, curr_sum, count):
    global sum_max
    if curr_sum > M:
        return

    if count == 3:
        if sum_max < curr_sum:
            sum_max = curr_sum
        return

    if index == N:
        return

    blackjack(index+1, curr_sum + num_list[index], count + 1)
    blackjack(index+1, curr_sum, count)

    return


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
sum_max = 0
blackjack(0, 0, 0)

print(sum_max)
```

### 3-2. ㅎㅅㅁ님 (백트래킹 부분집합)

```python
def pick_cards(start, cnt, total):
    global max_total

    # 가지치기
    if total > M:
        return

    # 기저조건
    if cnt == 3:
        if max_total < total:
            max_total = total
        return

    for i in range(start, N):
        pick_cards(i + 1, cnt + 1, total + numbers[i])


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
max_total = 0
pick_cards(0, 0, 0)
print(max_total)
```