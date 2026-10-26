import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

min_val = float('inf')
def recur(n, cnt):
    global min_val
    if n == 1:
        if min_val > cnt:
            min_val = cnt
        return
    if n % 3 == 0:
        recur(n//3, cnt+1)
    if n % 2 == 0:
        recur(n//2, cnt+1)
    recur(n-1, cnt+1)

N = int(input()) # 1 <= N <= 10^6
recur(N, 0)
print(min_val)
# ------------------
end = time.time()
print(end-start, '초')