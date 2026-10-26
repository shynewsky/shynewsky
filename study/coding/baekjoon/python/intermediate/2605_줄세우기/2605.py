import sys
sys.stdin = open('input.txt')

N = int(input()) # 학생 수
arr = list(map(int, input().split())) #

new = []
for i in range(N):
    cut = len(new) - arr[i]
    new = new[:cut] + [i+1] + new[cut:]

print(*new)

