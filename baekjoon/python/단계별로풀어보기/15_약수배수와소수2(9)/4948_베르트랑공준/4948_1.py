import time
start = time.time()
from pprint import pprint
# --------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write

# 1. 소수표(배열) 만들기
"""
n < 소수 <= 2n 인데
1 <= n <= 123456 이므로
"""
MAX = 246912
prime = [True] * (MAX + 1)  # 일단 모든 수는 소수라고 가정
prime[0] = prime[1] = False # 0과 1은 소수가 아니다

for i in range(2, int(MAX**0.5)+1): # 5*5=25 처럼 최대약수는 제곱근 이하이다

    if prime[i]: # 소수라고 가정하고 있을때

        for j in range(i*i, MAX+1, i): # i보다 작은 배수들은 이미 이전에 지워짐
            prime[j] = False # 소수로 가정한 수의 배수들은 소수가 아니므로 지워나간다

# 2. 누적합(배열)
"""
- 어떤 “구간 안에 있는 개수”를 계속 물어본다
- prefix[i] = i 이하의 소수 개수
"""
prefix = [0] * (MAX+1) # 0열은 패딩

for i in range(1, MAX+1): # 1열부터
    prefix[i] = prefix[i-1] + (1 if prime[i] else 0)

# 0. 입력

while True:
    n = int(input())
    if n == 0:
        break
    write(str(prefix[n*2] - prefix[n]) + '\n')

# --------------------
end = time.time()
write('\n'+str(end-start)+'초')
