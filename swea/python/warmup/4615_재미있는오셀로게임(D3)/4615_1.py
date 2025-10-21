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

        for nx, ny in dict[i]: # 같은 색상의 다른 돌 좌표 가져오기

            # 방향벡터 구하기
            dx, dy = nx-x, ny-y

            if dx != 0 :
                d = abs(dx) # 음수대비
                dx, dy = dx/d, dy/d
            elif dy != 0 : # dx == 0
                d = abs(dy) # 음수대비
                dx, dy = dx/d, dy/d

            # 8방향이 아니면 스킵
            if (dx, dy) not in delta:
                continue

            # 나누면서 float 가 되어서 다시 int 로 바꿔야 인덱스로 동작할 수 있다
            dx, dy = int(dx), int(dy)

            # 현재위치 좌표
            cx, cy = x, y

            # # 가는길에 0이 있는지 확인하기
            # isZero = False
            # while cx+dx != nx or cy+dy != ny:
            #
            #     # 현재 좌표이동
            #     cx += dx
            #     cy += dy
            #
            #     if mat[cx][cy] == 0:
            #         isZero = True
            #         break
            #
            # if isZero: # 하나라도 있으면 다음 타겟으로 변경
            #     continue
            #
            # # 현재위치 좌표(다시 받아오기)
            # cx, cy = x, y

            # 같은 색상의 다른 돌 좌표에 도달할때까지 이동
            while cx+dx != nx or cy+dy != ny:

                # 현재 좌표이동
                cx += dx
                cy += dy

                # 색상 다르면 바꾸기
                if mat[cx][cy] == ni: # 색상이 다르면
                    mat[cx][cy] = i   # 색상 반전
                    dict[ni].remove([cx, cy])   # 반대 색상에서 제거
                    new_stone.append([cx, cy])  # 바꾼 색상에 추가

                    # 개수 조절
                    if i == 1:
                        cnt_1 += 1
                        cnt_2 -= 1
                    else:
                        cnt_1 -= 1
                        cnt_2 += 1

            # 다음 이동을 위해 좌표 원위치
            cx, cy = x, y

        # 새로 추가된 돌 위치 추가
        dict[i] += new_stone

    # 출력 ---------------------------------------------------------------------------
    print(f'#{t}', cnt_1, cnt_2)
