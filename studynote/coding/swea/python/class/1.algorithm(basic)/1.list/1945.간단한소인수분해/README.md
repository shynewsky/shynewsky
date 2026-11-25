# ⭐다음 for문으로 넘어가기 위한 while 문 조건⭐

### for & while 문

```python
    base = [2, 3, 5, 7, 11]
    expo = [0, 0, 0, 0, 0]

    for i in range(5) :

        while N % base[i] == 0:
            N /= base[i]
            expo[i] += 1
```

---

### 첫코드

```python
    base = [2, 3, 5, 7, 11]
    expo = [0, 0, 0, 0, 0]

    isLoop = True
    while isLoop:
        if N % 2 != 0:
            isLoop = False
            break
        N /= 2
        a += 1

    isLoop = True

    while isLoop:
        if N % 3 != 0:
            isLoop = False
            break
        N /= 3
        b += 1

    isLoop = True

    while isLoop:
        if N % 5 != 0:
            isLoop = False
            break
        N /= 5
        c += 1

    isLoop = True

    while isLoop:
        if N % 7 != 0:
            isLoop = False
            break
        N /= 7
        d += 1

    isLoop = True

    while isLoop:
        if N % 11 != 0:
            isLoop = False
            break
        N /= 11
        e += 1

    print(f'#{test_case} {a} {b} {c} {d} {e}')
```