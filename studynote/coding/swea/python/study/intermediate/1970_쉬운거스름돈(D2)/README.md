# ⭐몫은 저장하고, 나머지는 돌린다⭐
# ⭐divmod() 활용⭐

### ✴️ 소인수분해 방법

```python
    divide = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(divide)):

        while N // divide[i] != 0: # 몫이 0이 될때까지
            change[i] = N // divide[i] # 몫은 채워 넣는다
            N -= (change[i] * divide[i]) # 나머지는 다시 돌린다
```

### ✴️ divmod() 활용

```python
    divide1 = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change1 = []

    for i in divide1 :
        div, mod = divmod(N, i) # div 몫, mod 나머지
        change1.append(div) # 몫은 채워넣는다
        N = mod # 나머지는 다시 돌린다
```


