T = int(input()) # 테스트 케이스 수

for test_case in range(1, T+1) :

    # 입력
    N = int(input()) # 행/열 수
    matrix = [list(map(int, input().split())) for _ in range(N)] # 행렬받기

    # 90도 회전 -> 2번하면 180도, 3번하면 270도
    matrix90 = list(zip(*matrix[::-1])) # 행을 역순으로 나열한 후 전치행렬 만들기
    matrix90 = [list(row) for row in matrix90] # 튜플 원소를 리스트 원소로 바꾸기

    matrix180 = list(zip(*matrix90[::-1])) # 행을 역순으로 나열한 후 전치행렬 만들기
    matrix180 = [list(row) for row in matrix180] # 튜플 원소를 리스트 원소로 바꾸기

    matrix270 = list(zip(*matrix180[::-1])) # 행을 역순으로 나열한 후 전치행렬 만들기
    matrix270 = [list(row) for row in matrix270] # 튜플 원소를 리스트 원소로 바꾸기

    # 출력
    print(f'#{test_case}')
    for i in range(N):  # 각 행 인덱스
        row1 = ''.join(map(str, matrix90[i]))
        row2 = ''.join(map(str, matrix180[i]))
        row3 = ''.join(map(str, matrix270[i]))
        print(row1, row2, row3)
