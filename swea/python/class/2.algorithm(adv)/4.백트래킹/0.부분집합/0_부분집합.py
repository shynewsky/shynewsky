# 부분집합1

import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().strip('{}').split(',')))
N = len(arr)

subset_list =[]
for i in range(1 << N):
    subset = []
    for j in range(N):
        if i & (1<<j):
            subset.append(arr[j])
    if sum(subset) == 10:
        subset_list.append(subset)

print(subset_list)

# 부분집합2

import sys
sys.stdin = open('input.txt')

def recur(n):

    if sum(path) == 10:
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

# 부분집합3

import sys
sys.stdin = open('input.txt')

def recur(n, path):

    if sum(path) == 10:
        print(*path)
        return

    # 중복없는 조합(1~10)
    for i in range(n, N):
        recur(i+1, path+[arr[i]]) # n+1 대신 i+1를 사용

arr = list(map(int, input().strip('{}').split(',')))
N = len(arr)

recur(0, [])

