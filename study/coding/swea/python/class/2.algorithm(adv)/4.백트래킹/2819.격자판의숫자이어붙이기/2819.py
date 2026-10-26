def recur(n):
    pass
    if n == M:
        string = ''
        for i in path:
            string += matrix[i[0]][i[1]]
            # print(matrix[i[0]][i[1])
        str_list.add(string)
        return

    if n == 0: # 시작점일때
        for i in range(N): # 기준점 행 순회
            for j in range(N): # 기준점 열 순회
                path.append([i,j])
                recur(n+1)
                path.pop()

    else: # 시작점이 아닐때
        for di, dj in delta:
            ni, nj = path[-1][0]+di, path[-1][1]+dj
            if 0<=ni<N and 0<=nj<N:
                path.append([ni,nj])
                recur(n+1)
                path.pop()

T = int(input())
for t in range(1, T+1):
    # 입력
    N, M = 4, 7 # 4x4, 7자리수
    matrix = [input().split() for _ in range(N)]
    # 변수
    delta = [[0, -1], [0, 1], [-1, 0], [1, 0]] # 동서남북
    path = []
    str_list = set()
    # 풀이
    recur(0) # 깊이 0부터 시작
    # 출력
    print(f'#{t}',len(str_list))

