import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 리스트 슬라이싱
# for _ in range(M):
#     a, b = map(int, input().split())
#     print(sum(numbers[a-1:b]))

# 누적합
for i in range(N-1):
    numbers[i+1] += numbers[i]

for _ in range(M):
    a, b = map(int, input().split()) # ~번째
    a, b = a-1, b-1 # 인덱스
    A = numbers[a-1] if a > 0 else 0
    B = numbers[b]
    print(B - A)

# ------------------
end = time.time()
print(end-start, '초')