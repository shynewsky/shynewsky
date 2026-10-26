def solution(board):
    n = len(board)  # board는 n*n 배열이므로, 행개수만 구해도 된다
    delta = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for i in range(n):  # 행순회
        for j in range(n):  # 열순회
            if board[i][j] == 1:  # 지뢰를 찾으면
                for di, dj in delta:  # 주변을 찾아서
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] != 1:  # 주변이 범위내에 있을때
                        board[ni][nj] = 2  # 2로 표시한다(지뢰와 겹치지 않게)

    count = 0
    for i in range(n):  # 행순회
        for j in range(n):  # 열순회
            if board[i][j] == 0:  # 안전한 지역일경우
                count += 1

    return count