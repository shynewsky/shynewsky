# ⭐(N-1) 을 더하고 N 으로 나눈 몫을 누적한다⭐

<br>

- break vs continue

```python
for i in range(N) :
   for j in range(M) : 
       break     # for i in range(N) 으로 나가서 i+1 로 간다
       continue  # for j in range(M) 으로 되돌아가서 j+1 로 간다
```

- 문제 유형 : "남아도 되는데 부족하면 안되는"
    - 피자 나누기 (프로그래머스) : 한판에 7개, 한명당 한조각 이상, n명일때 필요한 피자 수
    - 방 배정 (백준) : 한방에 3명, 한명당 한자리 이상, n명일때 필요한 방 수
- 문제 풀이 : 나누는 수보다 1 작은 수를 더한 후, 나눈 몫을 누적한다
    - count += (num + (M-1)) // M

```python
    return (n + (slice - 1)) // slice
```
```python
    count += (matrix[i][j] + (M-1)) // M
```

- 입력받는 방법 ㅡ ChatGPT 한테 물어봤을때, 이보다 간단한 방법이 없었다

```python
matrix = [[0] * 2 for _ in range(6)]

for _ in range(N) :
    gender, age = map(int, input().split())
    matrix[age-1][gender] += 1
```
