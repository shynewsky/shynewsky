# 시간 ------------------------------
import time
start = time.time()

# 입력 ------------------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write

# 함수 -----------------------------
def f(cnt):
    if cnt == M:
        write(" ".join(map(str, path)) + '\n')
        return

    for i in range(1, N1):
        if visited[i] == 1:
            continue
        visited[i] = 1
        path.append(i)
        f(cnt+1)
        path.pop()
        visited[i] = 0

# 변수 ------------------------------
N, M = map(int, input().split())
N1 = N+1 # lookup 비용 감소

# 코드 ------------------------------
path = []
visited = [0] * N1
f(0)

# 시간 ------------------------------
end = time.time()
print(end - start, '초')