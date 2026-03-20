'''
struct State → tuple (r, c)
queue 배열 → Python list + index
unordered_map → dict
vector<string> → list
방문 체크 → 2D 배열 유지
visit_cnt 트릭 그대로 유지
BFS 구조 그대로 유지
'''

from collections import deque

MAX_N = 100

board = [[0]*MAX_N for _ in range(MAX_N)]

distS = [[0]*MAX_N for _ in range(MAX_N)]
distE = [[0]*MAX_N for _ in range(MAX_N)]
visS = [[0]*MAX_N for _ in range(MAX_N)]
visE = [[0]*MAX_N for _ in range(MAX_N)]

str_vec = []
str_to_order = {}

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

NN = 0
MM = 0
visit_cnt = 0


def init(N, M, mGrade):
    global NN, MM, str_vec, str_to_order

    NN = N
    MM = M

    if not str_vec:
        for i in range(ord('A'), ord('Z')+1):
            str_vec.append(chr(i))

        for i in range(ord('A'), ord('Z')+1):
            for j in range(ord('A'), ord('Z')+1):
                str_vec.append(chr(i)+chr(j))

        for i in range(ord('A'), ord('Z')+1):
            for j in range(ord('A'), ord('Z')+1):
                for k in range(ord('A'), ord('Z')+1):
                    str_vec.append(chr(i)+chr(j)+chr(k))

        str_vec.sort()

        for i, s in enumerate(str_vec):
            str_to_order[s] = i

    for r in range(N):
        for c in range(N):
            board[r][c] = str_to_order[mGrade[r][c]]


def change(mRow, mCol, mDir, mLength, mGrade):
    val = str_to_order[mGrade]
    for d in range(mLength):
        r = mRow + dr[mDir]*d
        c = mCol + dc[mDir]*d
        board[r][c] = val


def calculate(L, sRow, sCol, eRow, eCol):
    global visit_cnt
    visit_cnt += 1

    lo = 0
    hi = len(str_vec) - 1
    ans = -1

    while lo <= hi:
        visit_cnt += 1
        mid = (lo + hi) // 2

        qS = deque([(sRow, sCol)])
        qE = deque([(eRow, eCol)])

        distS[sRow][sCol] = 0
        distE[eRow][eCol] = 0
        visS[sRow][sCol] = visit_cnt
        visE[eRow][eCol] = visit_cnt

        ok = False

        if board[eRow][eCol] < mid:
            hi = mid - 1
            continue

        while qS and qE:

            for _ in range(len(qS)):
                cr, cc = qS.popleft()
                dist = distS[cr][cc]

                if dist >= L:
                    continue

                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]

                    if not (0 <= nr < NN and 0 <= nc < NN):
                        continue

                    if board[nr][nc] < mid or visS[nr][nc] == visit_cnt:
                        continue

                    distS[nr][nc] = dist + 1
                    visS[nr][nc] = visit_cnt
                    qS.append((nr, nc))

                    if visE[nr][nc] == visit_cnt and distS[nr][nc] + distE[nr][nc] <= L:
                        ok = True
                        break

                if ok:
                    break
            if ok:
                break

            for _ in range(len(qE)):
                cr, cc = qE.popleft()
                dist = distE[cr][cc]

                if dist >= L:
                    continue

                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]

                    if not (0 <= nr < NN and 0 <= nc < NN):
                        continue

                    if not (nr == sRow and nc == sCol):
                        if board[nr][nc] < mid or visE[nr][nc] == visit_cnt:
                            continue

                    distE[nr][nc] = dist + 1
                    visE[nr][nc] = visit_cnt
                    qE.append((nr, nc))

                    if visS[nr][nc] == visit_cnt and distS[nr][nc] + distE[nr][nc] <= L:
                        ok = True
                        break

                if ok:
                    break
            if ok:
                break

        if ok:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return str_vec[ans]