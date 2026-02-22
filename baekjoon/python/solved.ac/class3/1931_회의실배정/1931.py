import time
start = time.time()
# --------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input()) # 1 <= N <= 100000
T = [list(map(int, input().split())) for _ in range(N)]

# 시작 시간이 빠른 순으로 정렬 X
# 끝나는 시간이 빠른 회의부터 선택 O
T.sort(key=lambda x: (x[1], x[0]))

cnt = 0
next = 0
for s, e in T:
    if next <= s:
        next = e
        cnt += 1

print(cnt)

# --------------------
end = time.time()
print(end-start, '초')