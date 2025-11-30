# ⭐split('0')⭐

### split(0)

```python
    N = int(input())
    str_arr = input().split('0')

    max_count = 0

    for i in range(len(str_arr)) : # 0으로 나누기 때문에, 기존 문자열 길이와 다르게 들어간다

        if not str_arr[i] : # 빈칸일 경우에 넘어가고
            continue

        count = 0
        for i in str_arr[i] : # 문자열을 분해하여 자릿수를 파악한다
            count += 1

        if max_count < count : # 최대를 구한다
            max_count = count
```

---

### max() 구현

```python
    count = 0
    max_count = 0

    for i in range(N) : # 배열 순회

        if str_list[i] == '1' :
            count += 1
        else :
            count = 0

        if max_count < count :
            max_count = count
```

---

### 첫코드

```python
    count_list = []
    count = 0
    count_num = 0
    
    if str_list[0] == '1' : 
        count += 1
    
    for i in range(N-1): 
        
        # 1을 찾으면 += 1
        if str_list[i+1] == '1' : # 1 이 아니라 '1' 로 작성해야한다
            count += 1
            
        # 0을 찾으면 append()
        elif str_list[i+1] == '0' : 
            count = 0

        count_list += [count]

    max_count = count_list[0]
    for i in range(len(count_list)) :
        if max_count < count_list[i] : 
            max_count = count_list[i]

    print(f'#{test_case} {max_count}')
```