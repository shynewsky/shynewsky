import sys
sys.stdin = open('input.txt')

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

N, K = map(int, input().split())
n1 = factorial(N)
n2 = factorial(N-K)
n3 = factorial(K)

print(n1 // (n2 * n3))
