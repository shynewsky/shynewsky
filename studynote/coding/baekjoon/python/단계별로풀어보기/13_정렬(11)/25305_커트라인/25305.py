import sys
sys.stdin = open('input.txt')

N, k = map(int, input().split())
li = sorted(list(map(int, input().split())), reverse=True)
print(li[k-1])
