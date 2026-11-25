### 카운팅 정렬

```python
    # 버스정류장 번호 최댓값 구해서
    # 지나가는 버스 정류장 번호를 모두 등록한 후
    # 등록된 횟수만큼 출력하기

    # 버스정류장 번호 최댓값 구하기
    # max_bussstop = max(buslane_list) 구현하기
    max_busstop = 0
    for low, top in buslane_list : # 버스정류장 번호 범위 가져오기, 이상/이하 언패킹하기
        if max_busstop < top :
            max_busstop = top

    # 버스정류장 번호 최댓값만큼 큰 배열 만들고, 지나가는 버스정류장 번호를 모두 등록한다
    count_list = [0] * (max_busstop + 1)  # 5번을 5번 인덱스에 등록하려면, 6칸을 만들어놔야한다
    for low, top in buslane_list :
        for busstop in range(low, top + 1): # 이하이기 때문에 +1 을 해줘야한다
            count_list[busstop] += 1

    # 버스정류장 번호
    print(f'#{test_case}', end=' ')
    for i in busstop_list:
        if 0 < i < len(count_list) : # 지나가지 않는 버정의 수가 존재할 수 있다 (작거나, 크거나)
            print(count_list[i], end=' ')
        else :
            print(0, end=' ') # 지나가지 않는 버정의 수는 0으로 출력한다

    if test_case != T:
        print()  # 줄바꿈 (마지막이 아니면)
```

---

### 배열

```python
    # 모든 버스정류장을 순서 상관없이 하나의 리스트에 모두 넣은 후
    # 찾은 횟수만큼 출력하기
    total_busstop = []
    for low, top in buslane_list :
        for busstop in range(low, top + 1) :
            total_busstop += [busstop]
   
    # 찾으려고 하는 버스 정류장만 출력한다
    print(f'#{test_case}', end=' ')
    for i in busstop_list :
        buscount = 0
        for j in total_busstop :
            if i == j :
                buscount += 1
        print(buscount, end=' ')

    if test_case != T:
        print()  # 줄바꿈 (마지막이 아니면)
```