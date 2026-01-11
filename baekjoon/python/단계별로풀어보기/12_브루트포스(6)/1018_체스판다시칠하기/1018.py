import sys
sys.stdin = open('input.txt')

# 입력 ----------------------------------------------------------

N, M = map(int, input().split())
mat = [list(input().strip()) for _ in range(N)]
# input().split() - ['WBWBWBWB']
# input().strip() - ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

# 코드 ----------------------------------------------------------

# 좌상단 이동
for i in range(N+1 - 8):
    for j in range(M+1 - 8):
        start = mat[i][j] #좌상단 좌표 저장

        # 부분행렬 이동
        for k in range(8):
            for l in range(8):
                pass




