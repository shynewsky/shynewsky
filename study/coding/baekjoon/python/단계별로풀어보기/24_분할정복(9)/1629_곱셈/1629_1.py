import time
start = time.time()
# --------------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write

# 0. 입출력
A, B, C = map(int, input().split())

# 1. 분할정복(=재귀함수)
def power(a, b):
    if b == 1:
        return a % C

    half = power(a, b // 2)

    if b % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * a) % C

write(str(power(A, B))+'\n')
# -------------------------
end = time.time()
write(str(end-start)+'초')