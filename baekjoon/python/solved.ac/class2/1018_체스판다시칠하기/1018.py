import time
start = time.time()
# -------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from pprint import pprint

N, M = map(int, input().split()) # 8~50 자연수
mat = [list(input().strip()) for _ in range(M)]

for i in range(N):
    for j in range(M):






# -------------------
end = time.time()
print(end-start, '초')