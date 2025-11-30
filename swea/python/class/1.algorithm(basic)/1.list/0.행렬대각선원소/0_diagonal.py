# 대각선 원소의 합
sum = 0
for i in range(N) : # 행 번호
    sum += matrix[i][i]
    sum += matrix[i][N-1-i]

if N % 2 == 1 :
    sum -= matrix[N//2][N//2]
