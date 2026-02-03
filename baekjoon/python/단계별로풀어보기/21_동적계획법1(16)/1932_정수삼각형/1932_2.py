# 타이머
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
# --------------------------------

# 입출력
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

# 동적계획법

# 1) 최솟값을 채운 배열 만들고, 첫 값만 먼저 채우기
dp = [-10**18] * N
dp[0] = costs[0][0]

# 2)
for i in range(1, N):
    temp_dp = [-10**18] * N
    for j in range(i+1):
        best = dp[j]
        if j-1 >= 0:
            best = max(best, dp[j-1])
        temp_dp[j] = best + costs[i][j]
    dp = temp_dp

print(max(dp[:N]))

# --------------------------------
# 타이머
end = time.time()
print(end-start, '초')