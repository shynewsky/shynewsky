T = int(input()) # 테스트 케이스

for test_case in range(1, T+1) :

    # 입력 받기
    # 이동단위 K개, 도착지 N, 충전기 M개
    K, N, M = map(int, input().split())   # 3 10 5
    arr = list(map(int, input().split())) # [1, 3, 5, 7, 9]

    # 정류장
    busstop_list = [0] * (N+1) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in arr :
        busstop_list[i] = 1    # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

    # 슬라이싱
    bus = 0    # 버스의 위치 (리스트 인덱스)
    charge = 0 # 충전 횟수

    while bus+K <= N :

        if bus+K >= N : # 도착하면 더이상 충전하지 않는다
            bus = N
            break

        # busstop_list[idx+K : idx : -1] : # K개씩 뜯어오는데, 뒤에서부터 1이 있는지 확인한다
        for i in range(bus+K, bus, -1):    # [1, 0, 1]
            if busstop_list[i] == 1:       # 뒷쪽에 가장 가까운 1을 찾아서 충전한다
                bus = i
                charge += 1
                break
        else : # 범위 내에 충전소가 없는데, 도착못했으면 0
            charge = 0
            break

    print(f'#{test_case} {charge}')
