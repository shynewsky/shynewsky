T = int(input())
for t in range(1, T+1):
    # 입력
    N = int(input()) # N개 사용신청
    matrix = [list(map(int, input().split())) for _ in range(N)] # S 작업시작시간, E 완료시간

    # 풀이 (회의실 예약)
    # 종료시간 기준으로, 오름차순 한다
    # 종료시간이 가장 빠른 회의를 찾자마자 확정한다
    # 이후 시작 가능한 회의 중, 가장 빨리 끝나는 회의를 찾아 확정한다

    # [E, S]로 만들기
    for i in range(N):
        matrix[i][0], matrix[i][1] = matrix[i][1], matrix[i][0]

    # E 기준으로 오름차순
    matrix.sort()

    # 시작할 수 있는 가장 빠른 회의부터 등록한다
    S = E = count = 0
    for end, start in matrix:
        if E <= start : # 이전 회의 종료시간보다 늦으면
            S, E = start, end
            count += 1

    # 출력
    print(f'#{t}',count)