T = int(input())

for test_case in range(1, T + 1):

    # 입력 받기
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 변수 설정 
    total_count = 0  # 연속된 1이 K 개인 횟수
    count = 0         # 연속된 1의 개수

    # 자신의 위치가 1 일때 count += 1
    # 자신의 위치가 0 이고, count == K 일때 total_count += 1
    
    # 행 에서 찾기 
    for i in range(N) : # 기준점 행 이동
        for j in range(N) : # 기준점 열 이동

            if matrix[i][j] == 1 : # 자신의 위치가 1 일때, 연속 1 증가
                count += 1
            elif matrix[i][j] == 0 :    # 자신의 위치가 0 일때
                if count == K :        # 지금까지 연속된 1이 K 개였을때, 단어 1 증가
                    total_count += 1  
                count = 0               # 연속된 1이 K가 아닐경우, 초기화

        if count == K :        # 지금까지 연속된 1이 K 개였을때, 단어 1 증가
            total_count += 1  
        count = 0 
        
    
    # 열 에서 찾기 
    for i in range(N) : # 기준점 열 이동
        for j in range(N) : # 기준점 행 이동

            if matrix[j][i] == 1 : # 자신의 위치가 1 일때, 연속 1 증가
                count += 1

            elif matrix[j][i] == 0 :    # 자신의 위치가 0 일때
                if count == K :        # 지금까지 연속된 1이 K 개였을때, 단어 1 증가
                    total_count += 1  
                count = 0               # 연속된 1이 K가 아닐경우, 초기화

        if count == K :        # 지금까지 연속된 1이 K 개였을때, 단어 1 증가
            total_count += 1  
        count = 0 
        
    print(f'#{test_case} {total_count}')