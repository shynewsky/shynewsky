# 숫자는 인덱스로, 횟수는 원소로 ⭐counts[arr[i]] += 1⭐

### max() 구현

```python
    max_num = 0    # 가장 많은 카드에 적힌 숫자
    max_count = 0  # 해당 카드가 몇장인지 출력

    for i in range(10) : # 0~9 까지 적힌 숫자

        # 최댓값 구하기
        count = 0
        for num in arr :  # 배열을 순회하며
            if num == i : # 같은 숫자가 몇개 있는지
                count += 1

        if max_count < count :
            max_count = count
            max_num = i
```

---

### 첫 코드 ㅡ 카운팅 정렬의 '숫자는 인덱스로, 횟수는 원소로' 나타내는 개념 활용

```python
    # 카운팅정렬
    counts = [0] * 10  # 0~9 까지의 숫자 카드
    for i in range(N) :
        counts[arr[i]] += 1

    # 최댓값 구하기
    max_idx = 0           # 가장 많이 나온 숫자
    max_count = counts[0] # 가장 많이 나온 숫자의 횟수

    for idx in range(10): # 인덱스로 counts 배열 순회

        if counts[max_idx] <= counts[idx] : # 횟수가 같다면 높은 숫자 반환
            max_idx = idx
            max_count = counts[idx]
```

---

### 코드 리뷰

- input() 배열 받아오기 ㅡ 리스트 컴프리헨션을 사용하면 \r 오류가 나지 않는다 (왜지?!)

```python
    #for char in input() :    # 문자열 분해
    for char in str(int(input())) :    # 문자열 분해 ㅡ \n 을 숫자로 변환할때 문제가 생김
        count_list[int(char)] += 1    # 인덱스가 숫자인 위치에 += 1 을 한다
```
```python
    arr = [int(x) for x in input()]  # list(map(int, input().split())) 이랑 같다
```

- COUNT 배열 만드는 방법

```python
    count = [0 for _ in range(10)] # [0] * 10 이랑 같다
```
```python
    counting_arr = [0] * (m + 1)  # max_v+1 : 4를 인덱스 4에 넣으려면 5개 배열을 만들어야해서
```

- COUNT 배열 채우기

```python
    for i in range(N):
        count[arr[i]] += 1  # 숫자에 해당하는 인덱스의 값을 1씩 올린다
```
