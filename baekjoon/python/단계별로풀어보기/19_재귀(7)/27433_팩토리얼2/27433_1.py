import sys
sys.stdin = open('input.txt')

N = int(input())

def recur(n):
    if n == 1:
        return 1
    return n * recur(n-1)

answer = recur(N)
print(answer)