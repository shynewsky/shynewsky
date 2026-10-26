## 학습 포인트 - 논리 제어

```python
#한 줄에 여러 데이터가 들어올때 입력 받는 방법
a, b = map(int, input().split())
```

```python
#조건문을 사용할때 'else if' 가 아니라 'elif' 를 사용한다
if : 
elif : 
else :
```

## 가장 짧은 코드

```python
T = int(input())

for test_case in range(1, T + 1):
    a,b = map(int,input().split())
    print(["","A","B"][a-b])
```