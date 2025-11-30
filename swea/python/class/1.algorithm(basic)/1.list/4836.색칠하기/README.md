# 빨강은 1, 파랑은 +1

```python
    # 칸 만들기
    board_matrix = [[0] * 10 for _ in range(10)]

    # 빨간색 찾기 = 1
    for i in range(N) :
        if input_list[i][4] == 1 : #color == red 일때
            for j in range(input_list[i][0], input_list[i][2]+1) : #이상, 이하 범위일때
                for k in range(input_list[i][1], input_list[i][3] +1): # 이상, 이하 범위일때
                    board_matrix[j][k] = 1  # 1로 대체한다

    # 파란색 += 1
    for i in range(N) :
        if input_list[i][4] == 2 : #color == blue 일때
            for j in range(input_list[i][0], input_list[i][2]+1) : #이상, 이하 범위일때
                for k in range(input_list[i][1], input_list[i][3] +1): #이상, 이하 범위일때
                    board_matrix[j][k] += 1   # 1을 더한다

    # 개수 구하기
    count = 0
    for i in range(10) :  # 전체 행렬을 돌며
        for j in range(10) :
            if board_matrix[i][j] > 1 :  # 1보다 큰 수를 찾는다
                count +=1    # 그 수가 보라색이다
```