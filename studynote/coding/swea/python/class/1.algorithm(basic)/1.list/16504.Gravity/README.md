# ⭐나보다 작은 박스의 개수⭐ = 낙차

### max() 구현

```python
    # 기준점 중심으로 오른쪽 높이가 낮으면, 낙차 +1 발생
    # i 로 기준점을 이동하고, j 로 비교점을 이동한다

    max_count = 0  # 최댓'값'만 구하는 것이므로 count 를 굳이 배열에 넣지 않아도 된다

    for i in range(N-1): # 마지막 인덱스에서는 낙차가 없음

        count = 0
        for j in range(i+1, N): # i<j 이므로 i+1 부터 순회
            if arr[i] > arr[j] :
                count += 1

        if max_count < count :
            max_count = count
```

### 첫 코드 ㅡ 카운팅 정렬 활용

- 첫번째 원소를 기준으로, 값이 같거나 큰 첫번째 원소를 찾는다
- 기준 값의 인덱스와, 대상 값의 인덱스의 차를 구한다
- 각 원소별 최대 낙차 값은 하나씩 나온다 ㅡ 크기가 N 인 배열을 만들어서, 낙차값만 저장한다


- 첫번째 원소를 기준으로, 값이 작은 원소를 만날때마다 +1 씩 증가하고
- 값이 같거나 큰 원소를 만나면 +0 씩 증가한다

```python
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):    
    N = int(input())                               
    box_list = list(map(int, input().split()))

    drop_list = [0] * N  # 낙차 값을 넣을 배열을 미리 선언한다

    # 나보다 작은 값을 찾으면, 배열값 증가
    for i in range(N) :
        for j in range(i+1, N) :
            if box_list[i] > box_list[j] :
                drop_list[i] += 1          

    # 최댓값 찾기
    max_drop = drop_list[0]
    for drop in drop_list :
        if max_drop < drop :
            max_drop = drop
 
    print(f'#{test_case} {max_drop}')
```
