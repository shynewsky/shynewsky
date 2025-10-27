import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 입력 -------------------------------------------------------
N = int(input()) # 색종이 수 (1<=N<=100)
data = [list(map(int, input().split())) for _ in range(N)]

# 코드 --------------------------------------------------------
'''
평면이 1001 * 1001 = 1천만이 넘어가므로, 1초 넘음. 즉, 최악의 경우 행렬사용불가
'''
mat = [[0] * 1001 for _ in range(1001)]
for n in range(N):
    x, y, h, w = data[n]
    for i in range(x, x+h):
        for j in range(y, y+w):
            mat[i][j] = n+1

for n in range(1, N+1):
    print(sum([row.count(n) for row in mat]))






