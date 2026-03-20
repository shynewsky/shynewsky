'''
❌ deque → 배열 큐 (B형 필수)
❌ tuple → 배열 (r,c 분리)
❌ len(q) 반복 → size 변수
❌ dict lookup 최소화
visit_cnt 그대로 유지 (초강력 최적화)
문자열 생성 최소화
'''

MAX_N = 100

board = [[0]*MAX_N for _ in range(MAX_N)]

distS = [[0]*MAX_N for _ in range(MAX_N)]
distE = [[0]*MAX_N for _ in range(MAX_N)]
visS = [[0]*MAX_N for _ in range(MAX_N)]
visE = [[0]*MAX_N for _ in range(MAX_N)]

str_vec = []
str_to_order = {}

dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

NN = 0
visit_cnt = 0


def init(N, M, mGrade):
    global NN

    NN = N

    if not str_vec:
        for i in range(65, 91):
            str_vec.append(chr(i))
        for i in range(65, 91):
            for j in range(65, 91):
                str_vec.append(chr(i)+chr(j))
        for i in range(65, 91):
            for j in range(65, 91):
                for k in range(65, 91):
                    str_vec.append(chr(i)+chr(j)+chr(k))

        str_vec.sort()

        for i in range(len(str_vec)):
            str_to_order[str_vec[i]] = i

    for r in range(N):
        row = board[r]
        for c in range(N):
            row[c] = str_to_order[mGrade[r][c]]


def change(mRow, mCol, mDir, mLength, mGrade):
    val = str_to_order[mGrade]

    drd = dr[mDir]
    dcd = dc[mDir]

    r = mRow
    c = mCol

    for _ in range(mLength):
        board[r][c] = val
        r += drd
        c += dcd


def calculate(L, sRow, sCol, eRow, eCol):
    global visit_cnt
    lo, hi = 0, len(str_vec) - 1
    ans = -1

    while lo <= hi:
        visit_cnt += 1
        mid = (lo + hi) >> 1

        if board[eRow][eCol] < mid:
            hi = mid - 1
            continue

        qSy = [0]*(MAX_N*MAX_N)
        qSx = [0]*(MAX_N*MAX_N)
        qEy = [0]*(MAX_N*MAX_N)
        qEx = [0]*(MAX_N*MAX_N)

        hs = ts = he = te = 0

        qSy[ts], qSx[ts] = sRow, sCol
        ts += 1

        qEy[te], qEx[te] = eRow, eCol
        te += 1

        distS[sRow][sCol] = 0
        distE[eRow][eCol] = 0
        visS[sRow][sCol] = visit_cnt
        visE[eRow][eCol] = visit_cnt

        ok = False

        while hs < ts and he < te:

            size = ts - hs
            for _ in range(size):
                cr = qSy[hs]
                cc = qSx[hs]
                hs += 1

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

                    qSy[ts], qSx[ts] = nr, nc
                    ts += 1

                    if visE[nr][nc] == visit_cnt and distS[nr][nc] + distE[nr][nc] <= L:
                        ok = True
                        break
                if ok:
                    break
            if ok:
                break

            size = te - he
            for _ in range(size):
                cr = qEy[he]
                cc = qEx[he]
                he += 1

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

                    qEy[te], qEx[te] = nr, nc
                    te += 1

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