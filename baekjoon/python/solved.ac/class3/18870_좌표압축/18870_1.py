import time
start = time.time()
# ------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input()) # 좌표 개수
arr = list(map(int, input().split())) # 좌표

types = sorted(set(arr)) # [-10, -9, 2, 4]
coord = {v : i for i, v in enumerate(types)} # {-10: 0, -9: 1, 2: 2, 4: 3}
print(*(coord[a] for a in arr))

# ------------------
end = time.time()
print(end-start, '초')