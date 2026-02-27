import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N = int(input()) # 1부터 N까지 카드

q = deque([i for i in range(1, N+1)])
while len(q) > 1:
    q.popleft() # 맨위 버리고
    q.append(q.popleft()) # 그다음은 아래로

print(*q)
# ------------------
end = time.time()
print(end-start, '초')