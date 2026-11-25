T = int(input())

for test_case in range(1, T + 1):

    # 입력 받기
    N, M = map(int, input().split()) #N행 M열
    matrix  = [list(map(int, input().split())) for _ in range(N)]
    
    # 델타
    delta = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    max_sum = 0
    
    for i in range(N): # 기준점 행 좌표
        for j in range(M): # 기준점 열 좌표
            count = matrix[i][j]
            sum = matrix[i][j]

            for di, dj in delta : # 방향벡터만큼
                for c in range(1, count+1) : #풍선 속 꽃가루가 팔길이가 된다
                    ni, nj = i + di * c, j + dj * c
                    
                    if 0<= ni < N and 0<= nj < M :  #ni는 행번호(N), nj는 열번호(M)
                        sum += matrix[ni][nj]
                        
            if max_sum < sum : 
                max_sum = sum
            
    print(f'#{test_case} {max_sum}')