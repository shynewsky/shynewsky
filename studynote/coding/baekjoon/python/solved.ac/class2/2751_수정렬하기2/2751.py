import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
numbers = sorted(list(int(input()) for _ in range(N)))
print('\n'.join(map(str, numbers)))