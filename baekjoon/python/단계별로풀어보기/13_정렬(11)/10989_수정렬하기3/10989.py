import sys
sys.stdin = open('input.txt')

N = int(input())
li = sorted([int(input()) for _ in range(N)])

for l in li :
    print(l)