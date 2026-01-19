# 타이머 -----------------------------
import time
start = time.time()

# 입출력 -----------------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write

# 함수 ------------------------------
def f(cnt, start):
    if cnt == M:
        write(" ".join(map(str, path)) + '\n')
        return
    
    for i in range(start, N1):
        if visited[i] == 1:
            break
        visited[i] = 1
        path.append(i)
        f(cnt+1, i+1)
        path.pop()
        visited[i] = 0

# 변수 ------------------------------
N, M = map(int, input().split())
N1 = N+1 # lookup 비용 절감

# 코드 ------------------------------
path = []
visited = [0] * N1
f(0, 1)

# 타이머 -----------------------------
end = time.time()
print(end-start, '초')