import time
start = time.time()
# --------------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write

# 0. 입출력
A, B, C = map(int, input().split())

# 1. (A^B)%C
def exp(a, b):
    ans = 1
    for _ in range(b):
        ans *= a
    return ans

ans = exp(A, B)
ans %= C
write(str(ans))
# -------------------------
end = time.time()
write(str(end-start)+'초')