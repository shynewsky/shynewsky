'''
struct → class
배열 → Python list
포인터(next, prev) → 인덱스 기반 유지
매크로 → 일반 함수/반복문
memset → 초기화
'''

# 1. 번역 버전

MAX = 100005

class G:
    def __init__(self, y, x, c, s, t, p, n):
        self.y = y
        self.x = x
        self.c = c
        self.s = s
        self.t = t
        self.p = p
        self.n = n

GP = [None] * MAX
BH = [[-1]*11 for _ in range(11)]
BW = [[0]*11 for _ in range(11)]
BA = [[0]*11 for _ in range(11)]
V = [[0]*1000 for _ in range(1000)]

GT = [0]*3
GC = 0
BS = 0


def II(y, x, ly, ry, lx, rx):
    return ly <= y <= ry and lx <= x <= rx

def GS(ct, t, c):
    return (ct - t) // GT[c]


def init(N, mGT):
    global GT, GC, BS
    GT = mGT[:]
    GC = 0

    BS = 1 if N == 10 else (10 if N <= 100 else 100)

    for i in range(1000):
        for j in range(1000):
            V[i][j] = 0

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

    GP[GC] = G(mRow, mCol, mCategory, -BW[y][x], mTime, -1, h)

    if h != -1:
        GP[h].p = GC

    BH[y][x] = GC
    GC += 1
    BA[y][x] += 1

    return 1


def water(mTime, Gv, mRow, mCol, mHeight, mWidth):
    res = 0

    by = mRow // BS
    bx = mCol // BS
    ey = (mRow + mHeight - 1) // BS
    ex = (mCol + mWidth - 1) // BS

    for sy in range(by, ey+1):
        for sx in range(bx, ex+1):

            l = sy * BS
            r = l + BS - 1
            a = sx * BS
            b = a + BS - 1

            if mRow <= l and mRow + mHeight - 1 >= r and mCol <= a and mCol + mWidth - 1 >= b:
                BW[sy][sx] += Gv
                res += BA[sy][sx]
            else:
                c = BH[sy][sx]
                while c != -1:
                    if II(GP[c].y, GP[c].x, mRow, mRow+mHeight-1, mCol, mCol+mWidth-1):
                        GP[c].s += Gv
                        res += 1
                    c = GP[c].n

    return res


def harvest(mTime, L, mRow, mCol, mHeight, mWidth):
    res = 0

    by = mRow // BS
    bx = mCol // BS
    ey = (mRow + mHeight - 1) // BS
    ex = (mCol + mWidth - 1) // BS

    for sy in range(by, ey+1):
        for sx in range(bx, ex+1):
            c = BH[sy][sx]
            while c != -1:
                if II(GP[c].y, GP[c].x, mRow, mRow+mHeight-1, mCol, mCol+mWidth-1):
                    if GS(mTime, GP[c].t, GP[c].c) + GP[c].s + BW[sy][sx] < L:
                        return 0
                    res += 1
                c = GP[c].n

    if res == 0:
        return 0

    for sy in range(by, ey+1):
        for sx in range(bx, ex+1):
            c = BH[sy][sx]
            while c != -1:
                nt = GP[c].n

                if II(GP[c].y, GP[c].x, mRow, mRow+mHeight-1, mCol, mCol+mWidth-1):
                    V[GP[c].y][GP[c].x] = 0
                    BA[sy][sx] -= 1

                    p = GP[c].p
                    n = GP[c].n

                    if p != -1:
                        GP[p].n = n
                    else:
                        BH[sy][sx] = n

                    if n != -1:
                        GP[n].p = p

                c = nt

    return res