# ⭐sum(map(int, str(i))) 로 자릿수합 구할수 있다⭐

### 완전탐색(반복문)

- 10으로 한번만 나눠도 1의 자리 수이다

```python
digits = []
while number > 0:
    digits.append(number % 10)
    number //= 10
return digits[::-1]
```

```python
# 입력
N = int(input())
# 변수
ans = 0
# 코드
for i in range(1, N+1):
    num = digits = i
    while num > 0:
        digits += num % 10
        num //= 10
    if digits == N:
        ans = i
        break
# 출력
print(ans)
```
<hr>

### 완전탐색(str)

- map을 활용해서 str인 숫자문자열을 int로 하나씩 분해해서, sum 으로 더해서 자릿수 합을 구한다

```python
sum(map(int, str(i)))
```

```python
# 입력
N = int(input())
# 코드
for i in range(1, N+1):
    if sum(map(int, str(i))) + i == N:
        print(i)
        break
else:
    print(0)
```
