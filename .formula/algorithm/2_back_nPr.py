# 중복순열

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

#--------------------------------------------------

# 순열

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
