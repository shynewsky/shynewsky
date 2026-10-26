import sys
sys.stdin = open('input.txt')

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b, gcd):
    return a * b // gcd

T = int(input())
for t in range(T):

    A, B = map(int, input().split())
    g = gcd(A, B)
    l = lcm(A, B, g)

    print(l)