import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = []
for idx in range(N):
    age, name = input().split()
    age = int(age)
    arr.append([age, idx, name])
arr.sort()
for age, idx, name in arr:
    print(age, name)
# ------------------
end = time.time()
print(end-start, '초')