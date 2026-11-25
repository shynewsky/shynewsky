import time
start = time.time()
# ----------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# N ≥ 1000 이면 재귀 깊이 제한을 초과
N = int(input())
N1 = N+1

# 1-1. 점화식 A(i) = A(i-1) + A(i-2) 로 DP 설계
if N == 1:
    print(1)
else :
    dp = [0] * N1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    print(dp[N])

# 1-2. 배열 없이 a, b 만 갖고 값 구하기
if N <= 2:
    print(N)
else:
    a, b = 1, 2 # dp[1], dp[2]
    for _ in range(3, N1):
        a, b = b, (a + b) % 10007
    print(b)

# ----------------
end = time.time()
print(end-start, '초')