T = 10 # 문제에서 주어진 테스트 케이스 수

for test_case in range(1, T+1) :

    # 입력 받기
    N = int(input()) # 테스트 케이스 번호
    M = 100 # 행/열 수
    matrix = [list(map(int, input().split())) for _ in range(M)] # 100*100 행렬 가져오기

    # 사다리타기
    # 특징) 거꾸로 해도 같은 점이 매칭된다

    # 행렬뒤집기
    # 100개면 49행과 50행이 교환 (정가운데 행 없음)
    # 101개면 50행 그대로, 49행과 51행 교환

    reverse_matrix = []
    for i in range(M-1, -1, -1) : # matrix 역순으로 순회
        reverse_matrix += [matrix[i]]

    # 2가 적힌 지점을 시작으로 출발 지점을 찾는다
    # reverse_matrix 의 [0] 행만 확인해도 된다

    x = 0 # 출발점 행
    y = 0 # 출발점 열

    for i in range(M) :
        if reverse_matrix[0][i] == 2 :
            y = i

    # 델타
    # 좌,우,하 방향벡터만 존재하고, 두 방향에서 1 을 찾으면, 좌우 우선으로 이동한다
    # 좌우 이동 후, 반드시 아래로 이동해야한다.
    # 지나온 길을 되돌아가는 것을 막기 위해, 지나온 길을 2 로 바꾼다 (출발점만 찾으면 되는것 뿐)

    delta = [[0, -1], [0, 1], [1, 0]] # 좌우하 방향벡터
    d = 0 # delta 리스트 인덱스

    # 기준점 위치 잡기
    # reverse_matrix[x][y]

    # 기준점을 중심으로, 주변 칸 확인하기

    isLoop = True
    while isLoop :
        way = 0
        for dx, dy in delta : # 좌우하 3방향 검색하기
            nx, ny = x + dx, y + dy # 손끝 좌표가 이러할때

            if 0<=nx<M and 0<=ny<M and reverse_matrix[nx][ny] == 1 : # 범위 안에 들어온 경우 & 1 인 경우
                reverse_matrix[x][y] = 2 # 왔던길 다시 돌아가지 못하게 막는 용도
                x, y = nx, ny
                break # 좌우 에 있으면 아래에 방향이 있어도 우선시. 바로 x,y 적용하고 for 문 탈출

        if x == M-1 :
            isLoop = False

    origin_x = M-1 -x
    origin_y = y

    print(f'#{test_case} {origin_y}')
