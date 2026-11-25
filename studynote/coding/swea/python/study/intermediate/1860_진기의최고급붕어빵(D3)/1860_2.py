T = int(input()) # 테스트케이스 수

for test_case in range(1, T+1):

    # 입력
    # N 사람, M 초마다, K 개
    # arr 도착하는 시간을 오름차순으로 나열하여 받아온다
    N, M, K = map(int, input().split())  # 2 2 2
    arr = sorted(list(map(int, input().split()))) # 3 4

    # 변수
    possible = True

    # 풀이
    # 정렬된 도착시간을 앞에서부터 확인한다
    # 인덱스(i)는 손님의 수, 값(v)은 손님의 도착 시간
    for c, t in enumerate(arr, start = 1): # [1,3] [2,4]
        if (t == 0             # 0초에는 아직 생상되지 않았음
            or (t//M)*K < c    # (t//M)*K : t초 까지의 누적 생산량이
        ):                     # 도착한 손님수보다 작으면, 적어도 한명은 대기해야하므로 불가능
            possible = False
            break

    print(f'#{test_case}', 'Possible' if possible else 'Impossible')
