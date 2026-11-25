import sys
sys.stdin = open('input.txt')

count = [0] * 10001

N = int(input())
for i in range(N):
    num = int(input())
    count[num] += 1
for i in range(10000000):
    for j in range(count[i]):
        print(i)
