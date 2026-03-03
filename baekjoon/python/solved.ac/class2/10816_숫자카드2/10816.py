import time
start = time.time()
# -------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
Nl = list(map(int, input().split())) # 전체
M = int(input())
Ml = list(map(int, input().split())) # 몇개있는지

cards = [0] * 20000001 # -10,000,000 <= Ml <= 10,000,000
for i in Nl:
    cards[i + 10000000] += 1
for i in Ml:
    print(cards[i + 10000000], end=' ')
# -------------------
end = time.time()
print(end-start,'초')