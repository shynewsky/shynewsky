import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 시간제약 15초
'''
순열
1. N번 만큼 열(W) 선택

상태트리
2. 아래(1,0)로 탐색하며 0이 아닌 칸 찾기
3. 칸에 적힌 수가 M 이라고 할때, (M-1)만큼 델타탐색
4. 상하좌우로 탐색하며 0이 아닌 칸 찾기

- 종료 : 깬 벽돌 최대 개수를 갱신하고
- 가지치기 : ... 어떻게 해야하지

- 최대한 많은 벽돌을 제거했을때, 남은 벽돌의 개수 구하기
'''

# 함수 --------------------------------------------------------------------------------


# 입력 --------------------------------------------------------------------------------

T = int(input()) # 테스트케이스
for t in range(1, T+1):
    N, W, H = map(int, input().split()) # N번(1<=N<=4), W*H 배열(2<=W<=12, 2<=H<=15)
    data = [list(map(int, input().split())) for _ in range(H)]
    # pprint(data)

    # 코드 ----------------------------------------------------------------------------

    # drop(0, []) # 구슬 떨어뜨리기 순열 코드



# def drop(n, path): # 구슬 번호
#     if n == N: # 구슬 N번 던지면
#         print(path)
#         return
#
#     i = 0 # 행은 0번
#     di, dj = (1, 0)  # 아래로 내려가면서 칸 정하기
#     for j in range(W): # 열 번호 정하면
#         while True:
#             ni, nj = i+di, j+dj
#             if 0<=ni<N and 0<=nj<N and data[ni][nj]:
#                 drop(n+1, path+[j])
#
#
#
# def break(i, j):
#     pass

# def break_brick(i, j): # 칸 안에 수
#     if data[i][j] == 1: # 칸 수가 1이면 탈출
#         return

#     for di, dj in delta:
#         for c in range(data[i][j]):
#             ni, nj = i+(di*c), j+(dj*c)
#             if 0<=ni<H and 0<=nj<W:
#                 break_brick(i+di, j+dj)
