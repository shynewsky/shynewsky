import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
hearX = set(input().strip() for _ in range(N))
seeX = set(input().strip() for _ in range(M))
inter = sorted(list(hearX & seeX))

print(len(inter))
for i in inter:
    print(i)