import time
start = time.time()
# ----------------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
from pprint import pprint

# 입출력
T = int(input())

# 소수를 뺀 나머지가 소수인지 확인하자

# 1. 소수 미리 만들기 (2 < N ≤ 1000000)
# - 에라토스테네스의 체가 전제

# 2. p를 2부터 N/2까지만 순회
# - N = p + q 에서 (p, q)와 (q, p)는 같은 경우

for _ in range(T):
    N = int(input())

# ----------------------------
end = time.time()
write(str(end-start)+'초')