import time
start = time.time()
# -------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    arr = sorted([a, b, c])
    if arr[2] ** 2 == (arr[0] ** 2) + (arr[1] ** 2):
        print('right')
    else:
        print('wrong')

# -------------------
end = time.time()
print(end-start, '초')