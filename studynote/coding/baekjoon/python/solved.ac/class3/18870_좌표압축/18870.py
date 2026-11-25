import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input()) # 좌표 개수
arr = list(map(int, input().split())) # 좌표

arr1 = [[i, x] for i, x in enumerate(arr)]  # [[0, 2], [1, 4], [2, -10], [3, 4], [4, -9]]
arr1.sort(key=lambda x: (x[1], x[0]))       # [[2, -10], [4, -9], [0, 2], [1, 4], [3, 4]]

base = arr1[0][1]   # Xi (기준)
cnt = 0             # Xj 개수

for i, x in arr1:
    if base < x:
        base = x
        cnt += 1
    arr[i] = cnt

print(*arr)
# ------------------
end = time.time()
print(end-start, '초')