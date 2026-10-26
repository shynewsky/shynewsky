T = int(input()) # 테스트케이스

for test_case in range(1, T+1) :

    # 입력받기
    # P : 전체 쪽수
    # Pa : A 가 찾아야 하는 쪽수
    # Pb : B 가 찾아야 하는 쪽수
    P, Pa, Pb = map(int, input().split())

    # A 찾기
    lowA = 1
    highA = P
    countA = 0

    while lowA <= highA : #

        countA += 1
        centerA = (lowA + highA) // 2
        if Pa == centerA : # 검색 성공
            break
        elif Pa < centerA : # 검색값이 왼쪽에 있을때
            highA = centerA   # 검색 범위를 왼쪽으로 이동
        elif Pa > centerA : # 검색값이 오른쪽에 있을때
            lowA = centerA    # 검색 범위를 오른쪽으로 이동

    # B 찾기
    lowB = 1
    highB = P
    countB = 0

    while lowB <= highB : #

        countB += 1
        centerB = (lowB + highB) // 2
        if Pb == centerB : # 검색 성공
            break
        elif Pb < centerB : # 검색값이 왼쪽에 있을때
            highB = centerB   # 검색 범위를 왼쪽으로 이동
        elif Pb > centerB : # 검색값이 오른쪽에 있을때
            lowB = centerB    # 검색 범위를 오른쪽으로 이동

    # A, B 비교하기
    if countA == countB :
        print(f'#{test_case} 0')
    elif countA < countB :
        print(f'#{test_case} A')
    elif countA > countB :
        print(f'#{test_case} B')