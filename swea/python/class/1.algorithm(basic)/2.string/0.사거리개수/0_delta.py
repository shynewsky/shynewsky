delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

total_count = 0 # 사거리 개수

for i in range(N):  # 기준점 행 이동
    for j in range(N):  # 기준점 열 이동

        count = 0 # 거리 개수 초기화

        for di, dj in delta : # 방향벡터 꺼내기
            ni, nj = i + di, j + dj # 주변 칸 검색

            # 전체행렬 범위에서 벗어나지 않을때,
            # 1 이 아닐때
            # 1(정수)가 아니라 '1'(문자열)로 비교해야함 ㅡㅡ 저번에도 틀렸던 부분
            if 0<=ni<N and 0<=nj<N and matrix[i][j] != '1' and matrix[ni][nj] != '1' :
                count += 1

        if count == 4 :
            total_count
