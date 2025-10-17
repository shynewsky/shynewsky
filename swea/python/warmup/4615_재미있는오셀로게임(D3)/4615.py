import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 입력
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]

    # 변수
    mat = [[0] * N for _ in range(N)]
    mat[N//2-1][N//2-1], mat[N//2-1][N//2], mat[N//2][N//2-1], mat[N//2][N//2] = 2, 1, 1, 2

    print(data)
    pprint(mat)

    # 코드
    for x, y, i in data:
        mat[x-1][y-1] = i

    pprint(mat)