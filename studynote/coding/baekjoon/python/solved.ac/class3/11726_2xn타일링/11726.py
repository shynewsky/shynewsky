import time
start = time.time()
# ----------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def func(summ):
    global count, N

    for i in range(1, 3): # 1,2
        if summ+i > N: # 가지치기
            return
        if summ+i == N:
            count += 1
            return
        func(summ+i)

count = 0
N = int(input())
func(0)
print(count)

# ----------------
end = time.time()
print(end-start, '초')