N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
arr = [i+1 for i in range(N)]

for i, j in matrix:
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

print(*arr)
