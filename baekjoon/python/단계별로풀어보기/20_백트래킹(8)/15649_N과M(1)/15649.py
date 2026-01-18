import sys
sys.stdin = open('input.txt')

# 함수 -----------------------------
def f(n):
    if n == M:
        print(*path)
        return

    for i in range(1, N+1):
        if visited[i] == 1:
            continue
        visited[i] = 1
        path.append(i)
        f(n+1)
        path.pop()
        visited[i] = 0

# 입력 ------------------------------
N, M = map(int, input().split())

# 코드 ------------------------------
path = []
visited = [0] * (N+1)
f(0)