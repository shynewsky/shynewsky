# 비트연산 ver.

import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split(', ')))
N = len(arr)

for i in range(1 << N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(arr[j])
    if sum(subset) == 0:
        print(subset)
