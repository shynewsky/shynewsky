T = int(input())
for test_case in range(1, T+1):

    # 입력
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 풀이
    # 행렬은 리스트 슬라이싱으로 풀 수 없다 ㅡ 부분행렬 혹은 델타로 푼다

    # 현재 위치가 (i, j)일 때,
    # (0,1)씩 더했을때, matrix[i][j+a]==0 이 되면, a 갱신 중단 ㅡ 횟수는 모르고 조건이 있으므로 while 사용
    # (1,0)씩 더했을때, matrix[i+b][j]==0 이 되면, b 갱신 중단 ㅡ 횟수는 모르고 조건이 있으므로 while 사용

    answer = []

    for i in range(N): # 기준점 행 순회
        for j in range(N): # 기준점 열 순회

            if matrix[i][j] != 0: # 기준점이 0이 아닌 숫자가 왔을때, 부분행렬 순회 시작

                # 길이 확인
                a = b = 0
                while matrix[i+a][j] != 0: # 아래로 뻗어본다
                    a += 1
                while matrix[i][j+b] != 0: # 오른쪽으로 뻗어본다
                    b += 1

                # 길이 확인했으면, 부분행렬 모두 0 으로 방문처리
                for p in range(a): # 부분행렬 행
                    for q in range(b): # 부분행렬 열
                        matrix[i+p][j+q] = 0

                answer.append([a*b, a, b])

    answer.sort() # 넓이가 작은것부터, 행이 작은것부터 ㅡ 오름차순 정렬

    print(f'#{test_case}', len(answer), *[x for row in answer for x in row[1:]]) # 리스트 슬라이싱으로 출력
