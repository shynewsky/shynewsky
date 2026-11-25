# 델타
delta = [[0, 1], [0, -1], [-1, 0], [1, 0]] # 방향벡터
count = 1

total_sum = 0 # 최댓값도 아니고, 그냥 누적이기 때문에, 변수 하나로도 충분

for i in range(N) : # 기준점 행 이동
    for j in range(N) : # 기준점 열 이동
        here = matrix[i][j]

        for di, dj in delta : # 방향벡터 꺼내기
            for c in range(1, count+1): # 팔길이 범위 (1이어도 공식 사용하기)
                ni, nj = i + di * c, j + dj * c

                if 0<=ni<N and 0<=nj<N : # 범위 제한하기
                    total_sum += abs(here - matrix[ni][nj])

