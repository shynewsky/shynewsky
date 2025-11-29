## 학습 포인트 - 완전 탐색

```python
#개수가 정해진 다수의 정수를 입력받는 방법
N, M = map(int, input().split()) 

#개수가 정해지지 않은 다수의 정수를 입력받는 방법
A = list(map(int, input().split()))
```

```python
print(f"#{test_case} {C[N-M]}")
```

## 가장 짧은 코드

```python
for _ in range(int(input())):
    n = list(map(int,input().split()))
    N = [[int(x)for x in input().split()],[int(x)for x in input().split()]]
    a = n[0]>n[1]
    b = n[not a] - n[a]
    print(f"#{_+1}",max([sum([N[a][i]*N[not a][i+j]for i in range(n[a])])for j in range(abs(a-b)+1)]))
```