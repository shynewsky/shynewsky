# AB/CD 모두 있는지 확인
# N*N 행렬이므로, 행/열 모두 N 사용 가능
# 다만, i+1 과 j+1 도 검사하므로, [N-1] 미만으로 순회해야한다

isABCD = False
for i in range(N-1) :
    for j in range(N-1) :
        if matrix[i][j] == 'A' and matrix[i][j+1] == 'B' and matrix[i+1][j] == 'C' and matrix[i+1][j+1] == 'D' :
            isABCD = True
            break

if isABCD :
    print('존재합니다.')
else :
    print('존재하지 않습니다.')

