# 재귀함수 ver.

import sys
sys.stdin = open('input.txt')

def recur(i, subset):

    if i == N: # 깊이
        if sum(subset) == 0:
            print(subset)
        return

    recur(i+1, subset) # 부분집합에 포함되지 않는 경우
    recur(i+1, subset+[arr[i]]) # 부분집합에 포함되는 경우


arr = list(map(int, input().split(', ')))
N = len(arr)
recur(0, [])
