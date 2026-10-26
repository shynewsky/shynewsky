import sys
sys.stdin = open('input.txt')

A = int(input())
B = int(input())
C = int(input())
M = str(A * B * C)

print(M.count('0'))
for i in range(1, 10): # 1~9
    print(M.count(str(i)))