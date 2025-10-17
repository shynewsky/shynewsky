N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

baguni = [0] * N
for i,j,k in matrix:
    for kan in range(i-1, j):
        baguni[kan] = k

print(*baguni)
