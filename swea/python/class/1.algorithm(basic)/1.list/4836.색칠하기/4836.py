# import sys
# sys.stdin = open('input.txt', 'r')
# from pprint import pprint

T = int(input())

for test_case in range(1, T + 1):

    # 입력 받기
    N = int(input())
    input_list = [list(map(int, input().split())) for i in range(N)]

    # 칸 만들기
    board_matrix = [[0] * 10 for _ in range(10)]

    # 빨간색 찾기 = 1
    for i in range(N) :
        if input_list[i][4] == 1 : #color == red 일때
            for j in range(input_list[i][0], input_list[i][2]+1) :
                for k in range(input_list[i][1], input_list[i][3] +1):
                    board_matrix[j][k] = 1

    # 파란색 += 1
    for i in range(N) :
        if input_list[i][4] == 2 : #color == blue 일때
            for j in range(input_list[i][0], input_list[i][2]+1) :
                for k in range(input_list[i][1], input_list[i][3] +1):
                    board_matrix[j][k] += 1

    # 개수 구하기
    count = 0
    for i in range(10) :
        for j in range(10) :
            if board_matrix[i][j] > 1 :
                count +=1

    print(f'#{test_case} {count}')
