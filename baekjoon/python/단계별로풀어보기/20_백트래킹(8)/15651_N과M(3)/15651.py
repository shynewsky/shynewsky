# 타이머 ---------------------------
import time
start = time.time()

# 입출력 ---------------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write

# 함수 -----------------------------
def f(n):

    pass

# 코드 ----------------------------
N, M = map(int, input().split())
print(N, M)

# 타이머 ---------------------------
end = time.time()
print(end-start, '초')