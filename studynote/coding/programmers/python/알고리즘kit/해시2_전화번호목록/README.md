## 1️⃣ 내 코드

- 총 시간복잡도 : 
- 리스트 슬라이싱 `phone_book[:i]` : O(N)
- 리스트 슬라이싱 `phone[:m]` : O(N)

```python
def solution(phone_book):
    n = len(phone_book)
    no_prefix = True
    for i in range(n):
        m = len(phone_book[i])
        for phone in phone_book[:i]:
            if phone_book[i] == phone[:m]:
                no_prefix = False
        for phone in phone_book[i+1:]:
            if phone_book[i] == phone[:m]:
                no_prefix = False
    return no_prefix
```

---

## 2️⃣ 효율적인 코드

1. 전치행렬 활용

```python
def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True

# - 총 시간복잡도 : O(n log n)
# - sort() : O(n log n)
# - startswith() : O(n)

'''
- sort() : 사전순으로 정렬하면, 접두어인 문자열이 바로 옆에 온다
["119", "97674223", "1195524421"]
["119", "1195524421", "97674223"]

- zip() : 
1회전: a="119", b="1195524421"
2회전: a="1195524421", b="97674223"

- b.startswith(a): b가 a로 시작하는지
'''
```

2. 집합 활용

```python
def solution(phone_book):
    s = set(phone_book)
    for num in phone_book:
        for i in range(1, len(num)):
            if num[:i] in s:
                return False
    return True

'''
- set() : 모든번호를 O(1)로 조회가능하게
S = {"119", "97674223", "1195524421"}

- for num in phone_book:
1회전: num="119"
    i=1 → num[:i]="1"
    i=2 → num[:i]="11"
    자기자신 전체 "119"는 검사하지 않음
2회전: num="97674223"
    i=1 → num[:i]="9"
    i=2 → num[:i]="97"
    ...
    i=7 → num[:i]="9767422"
3회전: num="1195524421"
    i=1 → num[:i]="1"
    i=2 → num[:i]="11"
    i=3 → num[:i]="119"
'''
```