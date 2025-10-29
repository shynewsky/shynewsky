## 학습 포인트

```python
#이렇게 하면 문자열로 저장하게 됨
a = list(input().split()) 

#이렇게 하면 정수형으로 저장하게 됨
a = list(map(int, input().split()))
```

```python
#버블소팅 안해도 오름차순/내림차순으로 정렬해줌
a.sort() #오름차순
a.sort(reverse=True) #내림차순

b = sorted(a) #오름차순
b = sorted(a, reverse=True) #내림차순
```

```python
#N이 항상 홀수이기 때문에 2로 나눈 몫은 항상 정가운데 숫자
mid = N // 2
```
## 가장 짧은 코드

```python
T = int(input())

for test_case in range(1, T + 1):

    n=input()
    print(sum(map(int, n)))
```