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
# import sys
# input = sys.stdin.readline
#
# MAX_N = 246912
#
# # 1. 에라토스테네스의 체
# is_prime = [True] * (MAX_N + 1)
# is_prime[0] = is_prime[1] = False
#
# for i in range(2, int(MAX_N ** 0.5) + 1):
#     if is_prime[i]:
#         for j in range(i * i, MAX_N + 1, i):
#             is_prime[j] = False
#
# # 2. 소수 개수 누적합
# prefix = [0] * (MAX_N + 1)
# for i in range(1, MAX_N + 1):
#     prefix[i] = prefix[i - 1] + (1 if is_prime[i] else 0)
#
# # 3. 입력 처리
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     print(prefix[2 * n] - prefix[n])

################################
end = time.time()
write(str(end-start) + '초')
