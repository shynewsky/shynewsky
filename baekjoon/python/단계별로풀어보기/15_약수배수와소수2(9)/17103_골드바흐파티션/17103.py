import time
start = time.time()
from pprint import pprint
# ----------------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write

# 1. 소수표(배열) 만들기 - 에레스토테네스의 체
MAX = 1000000
prime = [True] * (MAX + 1)  # 일단 모든 수는 소수라고 가정
prime[0] = prime[1] = False # 0과 1은 소수가 아니다

for i in range(2, int(MAX**0.5)+1): # 5*5=25 처럼 최대약수는 제곱근 이하이다
    if prime[i]: # 소수라고 가정하고 있을때
        for j in range(i*i, MAX+1, i): # i보다 작은 배수들은 이미 이전에 지워짐
            prime[j] = False # 소수로 가정한 수의 배수들은 소수가 아니므로 지워나간다

# 0. 입력
T = int(input())
for _ in range(T):
    n = int(input())

    # 2. 투포인터 - p를 2부터 N//2 까지만 순회
    "N = p + q 에서 (p, q)와 (q, p)는 같은 경우"
    cnt = 0
    for p in range(2, n//2+1):
        if prime[p] and prime[n-p]: # p와 n-p=q 가 모두 소수이면
            cnt += 1

    write(str(cnt)+'\n')

# ----------------------------
end = time.time()
write(str(end-start)+'초')