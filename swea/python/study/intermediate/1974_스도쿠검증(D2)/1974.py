T = int(input())

for test_case in range(1, T+1) : 
    
    # 입력받기
    matrix = [list(map(int, input().split())) for _ in range(9)] # 스도쿠 받기

    # 변수
    isGood = 1

    # 행 검사
    for i in range(9) : # 행 순회
        temp = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 소거할 리스트
        for j in range(9) : # 열 순회
            if matrix[i][j] in temp :
                temp.remove(matrix[i][j])
            else :
                isGood =0
                break

    # 열 검사
    for i in range(9) : # 열 순회
        temp = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 소거할 리스트
        for j in range(9) : # 행 순회
            if matrix[j][i] in temp :
                temp.remove(matrix[j][i])
            else :
                isGood =0
                break

    # 부분행렬 검사
    for i in range(0, 9, 3) : # 기준점 행 순회
        for j in range(0, 9, 3) :  # 기준점 열 순회
            temp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for k in range(3) : # 부분행렬 행 순회
                for l in range(3) : # 부분행렬 열 순회
                    if matrix[i+k][j+l] in temp :
                        temp.remove(matrix[i+k][j+l])
                    else :
                        isGood = 0
                        break
  
    print(f'#{test_case} {isGood}')

