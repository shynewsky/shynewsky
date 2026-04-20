import time
start = time.time()
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
# -------------------------------

L = int(input())
S = input().strip()

answer = 0
for i in range(L):
    alphabet = ord(S[i]) - ord('a') + 1
    answer += alphabet * (31 ** i)

print(answer % 1234567891)

# -------------------------------
end = time.time()
print(end-start, '초')