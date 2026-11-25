# 델타
delta1 = [[0, 1], [0, -1], [-1, 0], [1, 0]]   # + 모양
delta2 = [[1, 1], [1, -1], [-1, 1], [-1, -1]] # x 모양

max_fly = 0

# + 모양으로 뿌려보기
for i in range(N) : # 기준점 행 이동
    for j in range(N) : # 기준점 열 이동
        sum_fly = matrix[i][j] # 기준점

        for di, dj in delta1 : # 방향벡터 꺼내오기
            for c in range(1, M) : # 팔길이 늘리기 (0부터 시작하면 기준점 겹쳐서 더하게 된다)
                ni, nj = i + di * c, j + dj * c # 손끝 좌표

                if 0<=ni<N and 0<=nj<N : # 손끝이 범위 내에 있을때
                    sum_fly += matrix[ni][nj]

        if max_fly < sum_fly :
            max_fly = sum_fly

# x 모양으로 뿌려보기
for i in range(N) : # 기준점 행 이동
    for j in range(N) : # 기준점 열 이동
        sum_fly = matrix[i][j] # 기준점

        for di, dj in delta2 : # 방향벡터 꺼내오기
            for c in range(1, M) : # 팔길이 늘리기 (0부터 시작하면 기준점 겹쳐서 더하게 된다)
                ni, nj = i + di * c, j + dj * c # 손끝 좌표

                if 0<=ni<N and 0<=nj<N : # 손끝이 범위 내에 있을때
                    sum_fly += matrix[ni][nj]

        if max_fly < sum_fly :
            max_fly = sum_fly

print(max_fly)
