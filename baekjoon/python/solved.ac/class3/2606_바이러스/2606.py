import time
start = time.time()
# ---------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N = int(input()) # 컴퓨터 수
M = int(input()) # 연결된 쌍의 수

# 그래프 : 양방향 -> 연결리스트
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 탐색(BFS)
# 거리 문제가 아니라 감염된 개수여서
# visited[nx] = visited[x] + 1 을 사용하지 않음
q = deque()
visited = [0] * (N+1)

q.append(1) # 시작노드
visited[1] = 1

count = 0
while q:
    curr = q.popleft()

    for next in graph[curr]:

        if visited[next]:
            continue

        q.append(next)
        visited[next] = 1
        count += 1

print(count)
# ---------------------
end = time.time()
print(end-start, '초')