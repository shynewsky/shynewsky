import sys
input = sys.stdin.readline

N = int(input())
arr = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for j in range(y, y+h):
        arr[j][x:x+w] = [i]*w

for i in range(1, N+1):
    cnt = 0
    for j in range(1001):
        cnt += arr[j].count(i)
    print(cntㅍ)
