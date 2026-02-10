# 타이머
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
from pprint import pprint
# ------------------------------

N, M = map(int, input().split()) # N 크기, M 합 구하는 횟수
mat = [list(map(int, input().split())) for _ in range(N)]
sub = [list(map(int, input().split())) for _ in range(M)]

prefix =[[0] * N for _ in range(N)] # 누적합

# 열 수준에서 누적하기 - 0열 채우고, 1열부터
for i in range(N):
    prefix[i][0] = mat[i][0]
for i in range(N):
    for j in range(1, N):
        prefix[i][j] = prefix[i][j-1] + mat[i][j]
# 행 수준에서 누적하기 - 0행 있으니, 1행부터
for i in range(N):
    for j in range(1, N):
        prefix[j][i] = prefix[j-1][i] + prefix[j][i]
# 누적합 행렬 완료

for x1, y1, x2, y2 in sub:
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    p1 = prefix[x2][y2] # 42
    p2 = prefix[x1-1][y2] if x1 > 0 else 0 # 10
    p3 = prefix[x2][y1-1] if y1 > 0 else 0 # 6
    p4 = prefix[x1-1][y1-1] if (x1 > 0 and y1 > 0) else 0 # 1

    # print(x1, y1, x2, y2)
    # print(prefix[x2][y2])
    # print(prefix[x1-1][y2] if x1 > 0 else 0)
    # print(prefix[x2][y1-1] if y1 > 0 else 0)
    # print(prefix[x1-1][y1-1] if (x1 > 0 and y1 > 0) else 0)
    write(str(p1 - (p2 + p3) + p4) + '\n')

# ------------------------------
# 타이머
end = time.time()
write(str(end-start) + '초')