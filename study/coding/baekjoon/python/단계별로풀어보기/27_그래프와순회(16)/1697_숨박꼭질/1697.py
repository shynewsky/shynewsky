# 타이머
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
from pprint import pprint as pp
from collections import deque
# --------------------------------
# 입출력
N, K = map(int, input().split())

# BFS
q = deque()
q.append(N)

visited = [0] * 100001
visited[N] = 1

while q:
    c = q.popleft()

    # 동생 찾았으면 탈출
    if K == c:
        break

    for n in [c-1, c+1, c*2]:

        # 범위 밖일떄 패스
        if not (0<=n<=100000):
            continue

        # 방문했으면 패스 (무한순회 방지)
        if visited[n] != 0:
            continue

        q.append(n)
        visited[n] = visited[c] + 1

print(visited[K] - 1)

# 타이머
end = time.time()
print(end-start, '초')