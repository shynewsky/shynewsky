import time
start = time.time()
# -----------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def fibonacci(n):
    global cnt0, cnt1
    if n == 0:
        cnt0 += 1
        return 0
    elif n == 1:
        cnt1 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

T = int(input())
for _ in range(T):
    N = int(input())
    cnt0 = cnt1 = 0
    fibonacci(N)
    print(cnt0, cnt1)
# -----------------------
end = time.time()
print(end-start, '초')