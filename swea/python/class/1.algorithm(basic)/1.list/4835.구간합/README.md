# 값·인덱스만 구하는 거는 ⭐배열을 따로 만들 필요 없다⭐

### max() 구현

```python
    # 기준점(i)은 N까지 순회하며
    # 비교점(i+j)을 M개만큼 순회

    max_sum = 0
    min_sum = sum(arr) # 귀찮아서 그냥 sum() 사용함

    for i in range(N-M+1) : # 기준점 이동 (N-M이하 이므로, N-M+1 미만)

        cur_sum = 0
        for j in range(M) : # 이웃한 점 이동 (0부터 순회하면 i+j=i 가 되어버림)
            cur_sum += arr[i+j]

        if max_sum < cur_sum :
            max_sum = cur_sum
        if min_sum > cur_sum :
            min_sum = cur_sum
```

---

### 첫코드

```python
    # 합만 담긴 배열 만들기
    sum_list = []
    for i in range(0, N - M + 1):
        sum_num = 0
        for j in range(i, i + M):
            sum_num += data[j]
        sum_list += [sum_num]

    # 최댓값 구하기
    min_sum = sum_list[0]
    max_sum = sum_list[0]
    for i in range(0, len(sum_list)):
        if min_sum > sum_list[i]:
            min_sum = sum_list[i]
        if max_sum < sum_list[i]:
            max_sum = sum_list[i]

    print(f'#{test_case} {max_sum - min_sum}')
```