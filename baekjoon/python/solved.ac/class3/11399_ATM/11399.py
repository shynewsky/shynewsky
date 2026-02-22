import time
start = time.time()
# ----------------------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input()) # 줄 서 있는 사람 수
P = list(map(int, input().split())) # 돈 인출 시간

#각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값
Pa = sorted(P)
for i in range(N-1):
    Pa[i+1] += Pa[i]
print(sum(Pa))

# ----------------------------------
end = time.time()
print(end-start, '초')