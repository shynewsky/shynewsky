# Delta

### 델타

```python
T = int(input()) # 테스트케이스

for test_case in range(1, T+1) :

    N = int(input()) # 달팽이 N*N 수

    # 달팽이 숫자칸 만들기
    matrix = [[0] * N for _ in range(N)]
    num = 1
    matrix[0][0] = num 
    
    # 델타
    x, y, d = 0, 0, 0                           # 시작좌표 x y, 델타배열 첫 인덱스 d
    delta = [[0,1], [1, 0], [-1, 0], [0, -1]]  # [x % 4] 로 접근하면 좋을 듯 하다
	    
    # 가고자 하는 방향이 막혀있으면, 다음 delta 요소를 활용한다
    for _ in range(N**2 -1) : # 이동횟수는 항상 제곱수에서 -1 한 값	
        while True :      # 지금 방향으로 갈 수 없다면, 방향을 바꾸고, 그 방향도 막혀있다면 또 바꿔야한다
            dx = x + delta[d % 4][0]
            dy = y + delta[d % 4][1]

            if 0<= dx <N and 0<= dy < N and matrix[dx][dy] == 0 :
                x = dx
                y = dy
                num += 1
                matrix[dx][dy] = num
                break
            else :          # 방향만 바꾸고 이동하지 않음
                d += 1    # 방향 인덱스 다음으로 변경

       
    print(f"#{test_case}")
    for i in range(N):
        print(' '.join(map(str, matrix[i])))  # 행마다 출력
```

---

### 첫 코드

```python
# import sys
# sys.stdin = open('input.txt')
#from pprint import pprint

T = int(input()) # 테스트케이스

for test_case in range(1, T+1) :

    N = int(input()) # 달팽이 N*N 수

    # 달팽이 숫자칸 만들기
    matrix = [[0] * N for _ in range(N)]

    # 한방향으로 몇번씩 움직이는지, 배열로 만들기
    # N = 3 이면 [2, 2, 2, 1, 1]
    # N = 4 이면 [3, 3, 3, 2, 2, 1, 1]
    # N = 5 이면 [4, 4, 4, 3, 3, 2, 2, 1, 1,]
    distance_count = 2 * N - 1
    distance_list = [0] * distance_count
    distance_list[0] = N - 1

    minus = 1
    for i in range(1, distance_count - 1, 2) :
        distance_list[i] = N - minus
        distance_list[i+1] = N - minus
        minus += 1

    # 방향벡터 리스트 만들기
    # direction_list = []
    # for direction in [[0,1], [1,0], [0,-1], [-1,0]] :
    #     for i in distance_list:
    #         for _ in range(i) :
    #             direction_list += [direction]
    #         break

    vector_list = [[0,1], [1,0], [0,-1], [-1,0]]
    direction_list = []
    for count in range(distance_count) :
        # for distance in distance_list: 
        # for _ in range(distance) :
        for _ in range(distance_list[count]) :
            direction_list += [vector_list[count % 4]]
        # break

    # 현재 위치 이동하면서 글자 채워넣기
    num = 1
    row = 0
    column = 0
    matrix[row][column] = num

    for di, dj in direction_list :
        num += 1
        row += di
        column += dj
        matrix[row][column] += num

    print(f'#{test_case}')
    for row in matrix :
        for num in row :
            print(f'{num}', end=' ')
        print()
```