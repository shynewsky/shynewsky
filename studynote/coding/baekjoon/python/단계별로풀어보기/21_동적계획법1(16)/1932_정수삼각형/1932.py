# 타이머
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
# --------------------------------

def f(cnt, last, cost):
    global max_cost
    if cnt == N:
        if max_cost < cost:
            max_cost = cost
        return

    for i in range(cnt+1):
        if not (i == last or i == last+1):
            continue
        f(cnt+1, i, cost+costs[cnt][i])

# --------------------------------
# 입출력
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

# 코드
path = []
max_cost = 0
f(0, 0, 0)
print(max_cost)

# --------------------------------
# 타이머
end = time.time()
print(end-start, '초')