import sys
sys.stdin = open('input.txt')

'''
- 출발은 항상 (0,0), 도착은 항상 (N-1, N-1)
- 상하좌우 인접지역으로만 이동 가능
- 이동시 기본 1만큼 연료 소모, 높이 차이만큼 추가로 연료 소비

= 시작점 존재, 가중치의 최소합 => SPP(최단경로) 문제
'''

# 입력 -----------------------------------------------------------------------
T = int(input())
for t in range(1, T+1):
    N = int(input()) # N 행/열 수
    mat = [list(map(int, input().split())) for _ in range(N)] # N 지역높이

    print(mat)




