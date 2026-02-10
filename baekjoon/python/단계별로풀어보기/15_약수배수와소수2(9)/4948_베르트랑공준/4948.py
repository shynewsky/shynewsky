import time
start = time.time()
# --------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
# --------------------
from pprint import pprint
################################
# 함수
def prime(n):
    for i in range(2, n):
        if n % i == 0: # 나누어떨어지면 소수 아님
            return False
    return True # 한번도 약수가 없었으면 소수

# 입력
while True: # 무한 입력받기
    n = int(input())
    if not n: # 0이면 탈출
        break

    cnt = 0
    for i in range(n+1, n*2+1):
        if prime(i):
            cnt += 1

    write(str(cnt) + '\n')

################################
end = time.time()
write(str(end-start) + '초')
