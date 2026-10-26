import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:

    N = input().strip()
    if N == '0':
        break

    if N == N[::-1]:
        print('yes')
    else:
        print('no')

# ------------------
end = time.time()
print(end-start, '초')