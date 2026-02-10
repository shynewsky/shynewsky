# 타이머
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
from pprint import pprint
# ----------------------------------------

S = input().strip() # 문자열
q = int(input()) # 질문개수

# 보류

# ----------------------------------------
# 타이머
end = time.time()
write(str(end-start) + '초')