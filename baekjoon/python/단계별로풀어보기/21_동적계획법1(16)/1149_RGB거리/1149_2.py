# 타이머
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
from pprint import pprint
# ---------------------------------
# 입출력
N = int(input())
prices = [list(map(int, input().split())) for _ in range(N)]

# 코드
min_price = 1000 * N
# ---------------------------------
# 동적계획법

# 1) prices 크기의 빈 행렬을 만든다
dp = [[0] * 3 for _ in range(N)]

# 2) 첫번쨰 집이 빨강일때, 초록일때, 파랑일때의 sum을 모두 구한후
dp[0][0] = prices[0][0]
dp[0][1] = prices[0][1]
dp[0][2] = prices[0][2]

for i in range(1, N):
    dp[i][0] = prices[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = prices[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = prices[i][2] + min(dp[i-1][0], dp[i-1][1])

# 3) 빨/파/초 subtree의 sum 중 가장 작은 것을 고른다
min_price = min(dp[N-1][0], dp[N-1][1], dp[N-1][2])
print(min_price)
# ---------------------------------
# 타이머
end = time.time()
print(str(end-start) + '초\n')