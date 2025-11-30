T = int(input()) # 테스트 케이스 수

for test_case in range(1, T + 1):

    # 입력 받기
    N = int(input()) # 버스 노선 개수
    buslane_list = [list(map(int, input().split())) for _ in range(N)] # 버스정류장 번호 범위
    P = int(input()) # 버스정류장 개수
    busstop_list = [int(input()) for _ in range(P)] # 버스정류장 번호

    total_busstop = []
    for low, top in buslane_list :
        for busstop in range(low, top + 1) :
            total_busstop += [busstop]

    print(f'#{test_case}', end=' ')
    for i in busstop_list :
        buscount = 0
        for j in total_busstop :
            if i == j :
                buscount += 1
        print(buscount, end=' ')

    if test_case != T:
        print()  # 줄바꿈 (마지막이 아니면)
