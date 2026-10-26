import time
start = time.time()
# -------------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 0. 입력
N = int(input()) # 수의 개수
A = list(map(int, input().split())) # 피연산자
M = list(map(int, input().split())) # 연산자 개수
B = ['+'] * M[0] + ['-'] * M[1] + ['*'] * M[2] + ['/'] * M[3]




print(N, A, M, B)

# -------------------------
end = time.time()
print(end-start, '초')