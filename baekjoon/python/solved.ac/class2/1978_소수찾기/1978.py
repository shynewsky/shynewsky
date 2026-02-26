import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input()) # 수의 개수
arr = list(map(int, input().split()))

count = 0
for a in arr:

    if a == 1: # 1은 소수가 아님
        continue

    isPrime = True
    root = int(a ** 0.5) + 1

    for i in range(2, root):
        if a % i == 0 : # 나누어떨어지면 합성수
            isPrime = False
            break

    if isPrime:
        count += 1

print(count)
# ------------------
end = time.time()
print(end-start, '초')