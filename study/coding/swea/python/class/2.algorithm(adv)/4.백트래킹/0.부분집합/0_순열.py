import sys
sys.stdin = open('input.txt')

def recur(n):

    if len(path) == N:
        print(*path)
        return

    # 중복없는 순열(1~10)
    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        path.append(arr[i])
        recur(n+1)
        path.pop()
        visited[i] = 0

arr = list(map(int, input().strip('{}').split(',')))
N = len(arr)
path = []
visited = [0] * N

recur(0)
