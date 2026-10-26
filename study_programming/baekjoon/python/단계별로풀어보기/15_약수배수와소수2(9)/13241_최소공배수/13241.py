import sys
sys.stdin = open('input.txt')

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b, g):
    return a * b // g

A, B = map(int, input().split())
G = gcd(A, B)
L = lcm(A, B, G)
print(L)