import sys
sys.stdin = open('input.txt')

# 입력 ------------------------------------------------
T = int(input())
for t in range(1, T+1):
    N = int(input()) # 섬개수(1<=N<=1000)
    X = list(map(int, input().split())) # X좌표들(0<=X<=1000000)
    Y = list(map(int, input().split())) # Y좌표들(0<=Y<=1000000)
    E = float(input()) # 환경부담세율(0<=E<=1)

    # 전처리 -------------------------------------------
    islands = [(X[i], Y[i]) for i in range(N)]

    # union-find --------------------------------------
    # make_set : 자기자신을 원소로 갖는 집합
    '''
    {}
    '''



    print(islands)

