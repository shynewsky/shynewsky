'''
❌ class 제거 → 배열(flat list) 사용
❌ 객체 접근 → 인덱스 접근
지역변수 바인딩
반복 계산 제거
함수 호출 inline화
'''

# 2. 파이썬 최적화 버전

MAX = 100005

# 구조체 → 배열 분해
gy = [0]*MAX
gx = [0]*MAX
gc = [0]*MAX
gs = [0]*MAX
gtime = [0]*MAX
gp = [-1]*MAX
gn = [-1]*MAX

BH = [[-1]*11 for _ in range(11)]
BW = [[0]*11 for _ in range(11)]
BA = [[0]*11 for _ in range(11)]
V = [[0]*1000 for _ in range(1000)]

GT = [0]*3
GC = 0
BS = 0


def init(N, mGT):
    global GT, GC, BS

    GT[0], GT[1], GT[2] = mGT
    GC = 0

    BS = 1 if N == 10 else (10 if N <= 100 else 100)

    for i in range(1000):
        row = V[i]
        for j in range(1000):
            row[j] = 0

    for i in range(11):
        for j in range(11):
            BW[i][j] = 0
            BA[i][j] = 0
            BH[i][j] = -1


def sow(mTime, mRow, mCol, mCategory):
    global GC

    if V[mRow][mCol]:
        return 0

    V[mRow][mCol] = 1

    y = mRow // BS
    x = mCol // BS

    h = BH[y][x]

    gy[GC] = mRow
    gx[GC] = mCol
    gc[GC] = mCategory
    gs[GC] = -BW[y][x]
    gtime[GC] = mTime
    gp[GC] = -1
    gn[GC] = h

    if h != -1:
        gp[h] = GC

    BH[y][x] = GC
    BA[y][x] += 1

    GC += 1
    return 1


def water(mTime, Gv, mRow, mCol, mHeight, mWidth):
    res = 0

    by = mRow // BS
    bx = mCol // BS
    ey = (mRow + mHeight - 1) // BS
    ex = (mCol + mWidth - 1) // BS

    ry = mRow + mHeight - 1
    rx = mCol + mWidth - 1

    for sy in range(by, ey+1):
        for sx in range(bx, ex+1):

            l = sy * BS
            r = l + BS - 1
            a = sx * BS
            b = a + BS - 1

            if mRow <= l and ry >= r and mCol <= a and rx >= b:
                BW[sy][sx] += Gv
                res += BA[sy][sx]
            else:
                c = BH[sy][sx]
                while c != -1:
                    if mRow <= gy[c] <= ry and mCol <= gx[c] <= rx:
                        gs[c] += Gv
                        res += 1
                    c = gn[c]

    return res


def harvest(mTime, L, mRow, mCol, mHeight, mWidth):
    res = 0

    by = mRow // BS
    bx = mCol // BS
    ey = (mRow + mHeight - 1) // BS
    ex = (mCol + mWidth - 1) // BS

    ry = mRow + mHeight - 1
    rx = mCol + mWidth - 1

    # 검증
    for sy in range(by, ey+1):
        for sx in range(bx, ex+1):
            c = BH[sy][sx]
            while c != -1:
                if mRow <= gy[c] <= ry and mCol <= gx[c] <= rx:
                    if (mTime - gtime[c]) // GT[gc[c]] + gs[c] + BW[sy][sx] < L:
                        return 0
                    res += 1
                c = gn[c]

    if res == 0:
        return 0

    # 삭제
    for sy in range(by, ey+1):
        for sx in range(bx, ex+1):
            c = BH[sy][sx]
            while c != -1:
                nt = gn[c]

                if mRow <= gy[c] <= ry and mCol <= gx[c] <= rx:
                    V[gy[c]][gx[c]] = 0
                    BA[sy][sx] -= 1

                    p = gp[c]
                    n = gn[c]

                    if p != -1:
                        gn[p] = n
                    else:
                        BH[sy][sx] = n

                    if n != -1:
                        gp[n] = p

                c = nt

    return res