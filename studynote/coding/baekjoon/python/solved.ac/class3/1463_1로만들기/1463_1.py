import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
N1 = N + 1

dp = [0] * N1
for i in range(2, N1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])
# ------------------
end = time.time()
print(end-start, '초')