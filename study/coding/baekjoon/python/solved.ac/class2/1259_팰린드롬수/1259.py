import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:

    N = input().strip()
    if N == '0':
        break

    L = len(N)
    if L % 2 == 0: # 짝수일때
        for i in range(L//2):
            if N[i] != N[L-1-i]:
                print('no')
                break
        else:
            print('yes')
    if L % 2 == 1: # 홀수일때
        for i in range(L//2+1):
            if N[i] != N[L - 1 - i]:
                print('no')
                break
        else:
            print('yes')



# ------------------
end = time.time()
print(end-start, '초')