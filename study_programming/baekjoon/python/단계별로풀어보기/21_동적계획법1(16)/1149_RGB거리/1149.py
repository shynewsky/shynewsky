# 타이머
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
from pprint import pprint
# ---------------------------------

# 백트래킹
def f(cnt, color, price):
    global min_price
    if cnt == N:
        if min_price > price:
            min_price = price
        return
    for i in range(3):
        if i == color:
            continue
        if min_price < price+prices[cnt][i]:
            continue
        f(cnt+1, i, price+prices[cnt][i])

# ---------------------------------
# 입출력
N = int(input())
prices = [list(map(int, input().split())) for _ in range(N)]

# 코드
min_price = 1000 * N
f(0, -1, 0)
print(min_price)

# 타이머
end = time.time()
print(str(end-start) + '초\n')