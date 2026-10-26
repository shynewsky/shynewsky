import time
start = time.time()
from pprint import pprint
# -----------------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write

# 0. 입력
N = int(input())
mat = [list(map(int, input().strip())) for _ in range(N)]

# 1. 분할정복(=재귀함수)
'현재 영역이 모두 같은 값인지 확인 → 아니면 4등분 → 재귀'
def quad(r, c, size):
    lefttop = mat[r][c] # 비교기준
    """
    하나라도 다르다 
    = 서로 다른지 비교할 수도 있지만
    = 값 하나만 잡고 모든 값을 비교해도 결과는 같다
    """

    for i in range(r, r+size): # 행순회
        for j in range(c, c+size): # 열순회

            if lefttop != mat[i][j]: # 하나라도 다르면

                # 0. 출력
                write("(")

                # 1-1. 분할(4등분)
                half = size // 2
                quad(r, c, half)
                quad(r, c+half, half)
                quad(r+half, c, half)
                quad(r+half, c+half, half)

                # 0. 출력
                write(")")
                return

    # 모두 같으면 그대로 출력
    write(str(lefttop))

quad(0, 0, N)
# -----------------------------
end = time.time()
write('\n'+str(end-start)+'초')