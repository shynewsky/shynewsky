import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
사분면 분할 원리
r < mid <= r
c < mid <= c
'''

N, r, c = map(int, input().split())
side = 2 ** N # 한변의 길이
location = 0

while side > 1:
    mid = side // 2     # 중앙
    square = mid * mid  # 한 사분면에 있는 칸 개수

    if r < mid and c < mid : # 좌상단
        pass     # 그대로 타고 들어가기
    elif r < mid and mid <= c : # 우상단
        location += square
        c -= mid # 우상단 사분면으로 타고 들어가기
    elif mid <= r and c < mid: # 좌하단
        location += square * 2
        r -= mid # 좌하단 사분면으로 타고 들어가기
    elif mid <= r and mid <= c : # 우하단
        location += square * 3
        r -= mid # 우하단 사분면으로 타고 들어가기
        c -= mid

    side = mid # 한변의 길이 분할

print(location)
# ------------------
end = time.time()
print(end-start, '초')