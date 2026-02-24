import time
start = time.time()
# -------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input()) # 참가자 수
size = list(map(int, input().split())) # 신청자수
T, P = map(int, input().split()) # 티셔트 묶음 수, 펜 묶음 수

# 티셔츠 : s[i] 를 T로 나눈 몫 + 1
Tcnt = 0
for s in size:
    Tcnt += (s-1)//T + 1
print(Tcnt)

# 펜 : N을 P로 나눈 몫 + N을 P로 나눈 나머지
print(N//P, N%P)

# -------------------
end = time.time()
print(end-start, '초')