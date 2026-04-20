import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
arr.sort()
for a in arr:
    print(a)