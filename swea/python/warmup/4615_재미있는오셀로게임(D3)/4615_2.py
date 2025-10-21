import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 입력 ---------------------------------------------------------------------------------------
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # N 행/열 수, M 돌 놓는 횟수
    data = [list(map(int, input().split())) for _ in range(M)] # (x, y) color

    # 변수 -----------------------------------------------------------------------------------

    # 보드 초기화
    mat = [[0] * N for _ in range(N)]
    mat[N//2-1][N//2-1], mat[N//2-1][N//2], mat[N//2][N//2-1], mat[N//2][N//2] = 2, 1, 1, 2

    # 흑백 좌표 저장
    dict = {
        1 : [[N//2-1, N//2], [N//2, N//2-1]],
        2 : [[N//2-1, N//2-1], [N//2, N//2]],
    }

    # 흑백 개수 초기화
    cnt_1 = cnt_2 = 2 # black, white

    # 8방향 - 변경되는 변수가 아니면 튜플이 리스트보다 빠르다(?)
    delta = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

    # 코드 -----------------------------------------------------------------------------------

    # - 다음에 놓을 좌표를 받아온다
    # - 같은 색상의 돌 좌표를 확인하고, 해당 좌표까지의 방향벡터를 구한다
    # - 방향벡터로 이동하며 반대 색상은 반전시키고, 돌 개수도 갱신한다

    for a, b, i in data:

        # 인덱스로 변환
        x, y = a-1, b-1

        # 돌 올리기
        mat[x][y] = i

        # 돌 개수 추가
        if i == 1:
            cnt_1 += 1
        else:
            cnt_2 += 1

        # 루프돌면 dict[i] 리스트에 추가할 좌표들
        new_stone = [[x, y]]

        # 1일때 2, 2일때 1로 색상 전환
        # 2//i 를 하면 i=1 일때 2, i=2일때 1이 된다
        ni = 2//i

        # CHATGPT ----------------------------------------------------------

        # 8방향을 현재 놓은 자리에서 직접 검사: 인접칸이 상대색인지 먼저 확인
        for dx, dy in delta:
            cx, cy = x + dx, y + dy
            to_flip = []

            # 첫 칸이 보드 밖이거나 상대색이 아니면 해당 방향 무효
            if not (0 <= cx < N and 0 <= cy < N):
                continue
            if mat[cx][cy] != ni:
                continue

            # 상대색이 연속되는 동안 모아두고 진행
            while 0 <= cx < N and 0 <= cy < N and mat[cx][cy] == ni:
                to_flip.append((cx, cy))
                cx += dx
                cy += dy

            # 범위를 벗어나거나 0을 만나면 무효
            if not (0 <= cx < N and 0 <= cy < N):
                continue
            if mat[cx][cy] != i:  # 내 돌로 닫히지 않으면 무효
                continue

            # 여기까지 왔다면 사이의 상대색만 뒤집기
            for fx, fy in to_flip:
                mat[fx][fy] = i
                # dict 갱신 (방어적 제거)
                if [fx, fy] in dict[ni]:
                    dict[ni].remove([fx, fy])
                new_stone.append([fx, fy])

                # 개수 갱신
                if i == 1:
                    cnt_1 += 1
                    cnt_2 -= 1
                else:
                    cnt_1 -= 1
                    cnt_2 += 1

        # CHATGPT ----------------------------------------------------------

        # 새로 추가된 돌 위치 추가
        dict[i] += new_stone

    # 출력 ---------------------------------------------------------------------------
    print(f'#{t}', cnt_1, cnt_2)
