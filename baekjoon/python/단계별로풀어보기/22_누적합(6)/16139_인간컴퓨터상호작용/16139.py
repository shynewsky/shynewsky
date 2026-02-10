# 타이머
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
# ----------------------------------------

S = input() # 문자열
q = int(input()) # 질문의수
# 질문 : [l, r+1] 구간에서의 a의 개수
for _ in range(q):
    a, l, r = input().split()
    write(str(S[int(l):int(r)+1].count(a)) + '\n')

# ----------------------------------------
# 타이머
end = time.time()
write(str(end-start) + '초')