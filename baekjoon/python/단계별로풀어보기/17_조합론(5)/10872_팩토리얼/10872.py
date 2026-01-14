import sys
sys.stdin = open('input.txt')

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

N = int(input())
print(factorial(N))

