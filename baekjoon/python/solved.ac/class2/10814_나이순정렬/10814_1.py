import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [input().split() for _ in range(N)]
arr.sort(key=lambda x : int(x[0]))
for a in arr:
    print(*a)
# ------------------
end = time.time()
print(end-start, '초')