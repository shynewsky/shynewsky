import time
start = time.time()
# -------------------
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from pprint import pprint

N, M = map(int, input().split()) # 8~50 자연수
board = [input().strip() for _ in range(M)]

board_white = [
    'WBWBWBWB',
    'BWBWBWBW',    
    'WBWBWBWB',
    'BWBWBWBW',    
    'WBWBWBWB',
    'BWBWBWBW',    
    'WBWBWBWB',
    'BWBWBWBW',    
]
board_black = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
]

for i in range(N):
    for j in range(M):
        first = board[i][j]
        wrong = False

        if first == 'W':
            for k in range(8):
                for l in range(8):
                    if board[i+k][j+l] != board_white[k][l]:
                        wrong = True
                        break
                if wrong:
                    break
        elif first == 'B':
            for k in range(8):
                for l in range(8):
                    if board[i+k][j+l] != board_black[k][l]:
                        wrong = True
                        break
                if wrong:
                    break

# -------------------
end = time.time()
print(end-start, '초')