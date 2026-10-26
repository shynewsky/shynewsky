import time
start = time.time()
# --------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def func(n, summ):
    global count, N

    for i in range(1,4):
        if summ+i > N: # 가지치기
            return
        if summ+i == N: # 종료조건
            count += 1
            return
        func(n+1, summ+i)

T = int(input()) # 테스트케이스 수

for _ in range(T):
    count = 0
    N = int(input())
    func(0, 0)
    print(count)

# --------------------
end = time.time()
print(end-start, '초')