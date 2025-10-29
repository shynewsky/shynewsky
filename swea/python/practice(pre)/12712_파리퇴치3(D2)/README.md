## 학습 포인트 - 배열제어, 😭예외처리, 4중for문

```python
#for 문으로 리스트 원소들이 좌표일때, x와 y 좌표를 동시에 가져올 수 있다

for x, y in [(-m, 0), (m, 0), (0, -m), (0, m)] :
    spray_x = row + x  #뿌려지는 칸의 행 번호
```

```python
#행렬의 칸을 예외처리하는 방법은, 행 인덱스와 열 인덱스의 범위를 지정한느 것
#기본적으로 모든 칸을 제외시키고, 조건에 통과한 칸만 포함시키는 방법

if  0 <= spray_x <= N and 0 <= spray_y <= N 
    sum_perpendicular += matrix[spray_x][spray_y]
```

```python
#max() 함수를 활용하여, 여러 수 중에 가장 큰 수를 찾을 수 있다
#min() 함수도 마찬가지로, 여러 수 중에 가장 작은 수를 찾을 수 있다

max_kill = max(max_kill, sum_plus, sum_cross)
```

<br>

- 시간 복잡도 계산법

```python
for i in range(N):              # O(N)
    for j in range(N):          # O(N)
        for d in range(1, M):   # O(M)
            # 방향 4개 반복 → 상수 (4번 반복하므로 O(1))

O(N * N * M * 4) = O(N²M)
```

## 가장 짧은 코드

```python
for _ in range(int(input())):
    n,m = map(int,input().split())
    n,m = range(n),range(-m+1,m)
    N = [[int(x) for x in input().split()] for _ in n]
    i = [[[p+a,q] for a in m if p+a in n]+[[p,q+a] for a in m if q+a in n and a!=0] for p in n for q in n]
    j = [[[p+a,q+b]for a in m for b in m if abs(a)==abs(b) and p+a in n and q+b in n] for p in n for q in n]
    print(f"#{_+1} {max([sum([N[x][y]for x,y in a])for a in i]+[sum([N[x][y]for x,y in a])for a in j])}")
```