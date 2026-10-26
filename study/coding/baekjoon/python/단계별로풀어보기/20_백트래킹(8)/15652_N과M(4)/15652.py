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
        path.append(i)
        f(cnt+1, i)
        path.pop()

# 코드 ------------------------------
N, M = map(int, input().split())
N1 = N+1

path = []
f(0, 1)

# 타이머 -----------------------------
end = time.time()
print(end-start, '초')


