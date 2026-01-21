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
    global min_price, count

    if cnt == N: # 종료조건
        if min_price > price : # 최소값 갱신
            min_price = price
        count += 1
        print(min_price)
        return

    for i in range(3): # 빨초파
        if i == color: # 가지치기
            continue
        # if price+prices[cnt][i] > min_price: # 가지치기
        #     continue
        f(cnt+1, i, price+prices[cnt][i])


# ---------------------------------
# 입출력
N = int(input())
prices = [list(map(int, input().split())) for _ in range(N)]
min_price = 1000 * N
count = 0
pprint(prices)

f(0, 0, 0)

print(count)

# 타이머
end = time.time()
print(str(end-start) + '초\n')