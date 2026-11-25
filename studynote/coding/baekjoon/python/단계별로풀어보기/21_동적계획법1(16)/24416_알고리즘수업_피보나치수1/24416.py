# 타이며
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
# ------------------------------------
# 함수
cnt1 = 0
def f1(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    return f1(n-1) + f1(n-2)

cnt2 = 0
def f2(n):
    global cnt2
    dp = [0] * N1
    dp[1] = dp[2] = 1
    for i in range(3, N1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt2 += 1
    return dp[n]

# ------------------------------------
# 입출력
N = int(input())
N1 = N+1

f1(N)
f2(N)

write(str(cnt1) + '\n')
write(str(cnt2) + '\n')

# 타이머
end = time.time()
write(str(end-start) + '초\n')