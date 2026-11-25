# ⭐역으로 내려오면서, 최댓값일때 갱신하거나, 이익을 누적하거나⭐

### 1️⃣ 시간복잡도 : O(N^2)

|  |  |
| --- | --- |
| arr = data[idx:] | O(N-idx) |
| max(data[idx:]) | O(N-idx) |
| arr.index(max_num) | O(N-idx) |

<hr>

### 2️⃣ 효율적인 코드 : O(N)

- 미래에서부터 "지금까지 본 최고가" 유지
- 오늘 가격이 최고가보다 낮으면 그 차이만큼 이익 (오늘 산걸 미래 최고가에 판 가격)을 더한다
- 최댓값을 다시 찾을 필요가 없으니, 한번의 역방향 순회로 끝난다

```python
T = int(input())
for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    
    max_future = 0
    profit = 0
    for p in reversed(prices):          # 오른쪽 → 왼쪽 한 번만 순회
        if p >= max_future:
            max_future = p              # 앞으로 팔 최고가 갱신
        else:
            profit += (max_future - p)  # 오늘 사서 미래 최고가에 파는 이익
    
    print(f'#{t}', profit)
```

<hr>

- 예1) [10, 7, 6]
```
6 일때 - 최고가 6
7 일때 - 최고가 7
10일때 - 최고가 10
이익 = 0
```
- 예2) [3, 5, 9]

```
9일때 - 최고가 9
5일때 - 이익 +(9-5)
3일때 - 이익 +(9-3)
이익 = 10
```
- 예3) [1, 1, 3, 1, 2]
```
2일때 - 최고가 2
1일때 - 이익 +(2-1)
3일때 - 최고가 3
1일때 - 이익 +(3-1)
1일때 - 이익 +(3-1)
이익 = 5
```