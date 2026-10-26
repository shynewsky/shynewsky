import time
start = time.time()
# -------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input()) # 자연수N
A = list(map(int, input().split()))
M = int(input()) # 수 개수
X = list(map(int, input().split()))

# 전체 방명록 (-2^31 ~ 2^31)
dict = {}
for a in A:
    dict[a] = 1
for x in X:
    try : print(dict[x])
    except : print(0)

# -------------------
end = time.time()
print(end-start, '초')