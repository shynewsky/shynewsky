import time
start = time.time()
# --------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

"""
- 무방향(양방향)
- 연결요소 개수 구하기
"""

# 입력
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 변수
q = deque()
visited = [0] * (N+1)
count = 0

for i in range(1, N+1):

    if visited[i] == 1:
        continue

    count += 1
    q.append(i)
    visited[i] = 1

    while q:
        c = q.popleft()

        for n in graph[c]:

            if visited[n] == 1:
                continue

            q.append(n)
            visited[n] = 1

print(count)
# --------------------
end = time.time()
print(end-start, '초')