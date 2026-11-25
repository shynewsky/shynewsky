import sys
sys.stdin = open('input.txt')

def recur(n):

    if len(path) == N:
        print(*path)
        return

    # 중복순열(1~10)
    for i in range(N):
        path.append(arr[i])
        recur(n+1)
        path.pop()

arr = list(map(int, input().strip('{}').split(',')))
N = len(arr)
path = []

recur(0)
