import sys
sys.stdin = open('input.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x: (x[1], x[0]))

for x, y in data: # print() 안에 for 는 안 씀
    print(x, y)