import sys
sys.stdin = open('input.txt')

def recur(n):

    if len(path) == 3:
        print(*path)
        return

    # 중복없는 조합(1~10)
    for i in range(n, N):
        path.append(arr[i])
        recur(i+1) # n+1 대신 i+1를 사용
        path.pop()

arr = list(map(int, input().strip('{}').split(',')))
N = len(arr)
path = []

recur(0)