N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = [[0] * M for _ in range(N)]

for i in range(N): # 행순회
    for j in range(M): # 열순회
        C[i][j] = A[i][j] + B[i][j]

for i in range(N):
    for j in range(M):
        print(C[i][j], end=' ')
    print()
