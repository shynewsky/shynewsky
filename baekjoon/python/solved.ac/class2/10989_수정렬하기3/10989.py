import sys
sys.stdin = open('input.txt')



10,000,000


N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
arr.sort()
for a in arr:
    print(a)