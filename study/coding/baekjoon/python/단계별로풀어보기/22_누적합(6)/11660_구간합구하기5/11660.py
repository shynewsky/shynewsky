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

# 부분행렬
for x1, y1, x2, y2 in sub:
    prefix = 0
    for x in range(x1-1, x2):
        for y in range(y1-1, y2):
            prefix += mat[x][y]
    print(prefix)

# ------------------------------
# 타이머
end = time.time()
write(str(end-start) + '초')