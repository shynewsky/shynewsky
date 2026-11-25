import copy #리스트는 참조를 할당하기 때문에, 깊은 복사로 복사해야한다

T = int(input()) #테스트케이스 개수

for test_case in range(1, T + 1):
    
    #행렬만들기 ----------------------------------------------------
    #행을 먼저 받은 후, 행을 쌓아서 열을 만든다

    N = int(input()) #행/열 개수
    matrix = list() #빈 행렬 선언

    for _ in range(0, N) : #열 개수 만큼 반복
        row = list(map(int, input().split())) #행 원소 입력
        matrix.append(row)

    #회전시키기 ----------------------------------------------------
    #0열이 0행이 되고, 1열이 1행이 되고, 2열이 2행이 되고...
    
    matrix_90 = copy.deepcopy(matrix)     #임의로 같은 크기의 행렬을 만들기 위함
   
    for i in range(N) : 
        for j in range(N) :    #range(0,N)==range(N)
            matrix_90[i][-1-j] = copy.deepcopy(matrix[j][i])

    matrix_180 = copy.deepcopy(matrix) 
            
    for i in range(N) : 
        for j in range(N) : 
            matrix_180[i][-1-j] = copy.deepcopy(matrix_90[j][i])
            
    matrix_270 = copy.deepcopy(matrix) 
            
    for i in range(N) : 
        for j in range(N) : 
            matrix_270[i][-1-j] = copy.deepcopy(matrix_180[j][i])
     
    #출력하기

    print(f'#{test_case}')
    for i in range(N):  # 각 행 인덱스
        row1 = ''.join(map(str, matrix_90[i]))
        row2 = ''.join(map(str, matrix_180[i]))
        row3 = ''.join(map(str, matrix_270[i]))
        print(row1, row2, row3)