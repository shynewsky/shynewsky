#include <memory.h>
 
#define FR(i,s,e) for(register int i=(s);i<=(e);++i)
#define WH(c) while((c)!=-1)
#define GP grain_pool
#define BH bucket_head
#define BW bucket_water
#define BA bucket_alive
#define RN mRow, (mRow+mHeight-1), mCol, (mCol+mWidth-1)
 
struct G { int y, x, c, s, t, p, n; } GP[100005];
int BH[11][11], BW[11][11], BA[11][11], V[1000][1000], GT[3], GC, BS;
 
inline bool II(int y, int x, int ly, int ry, int lx, int rx) { return y >= ly && y <= ry && x >= lx && x <= rx; }
inline int GS(int ct, int t, int c) { return (ct - t) / GT[c]; }
 
void init(int N, int mGT[]) {
    FR(i, 0, 2) GT[i] = mGT[i]; GC = 0;
    BS = (N == 10) ? 1 : (N <= 100 ? 10 : 100);
    memset(V, 0, sizeof(V)); memset(BW, 0, sizeof(BW));
    memset(BA, 0, sizeof(BA)); memset(BH, -1, sizeof(BH));
}
 
int sow(int mTime, int mRow, int mCol, int mCategory) {
    if (V[mRow][mCol]) return 0; V[mRow][mCol] = 1;
    int y = mRow / BS, x = mCol / BS, h = BH[y][x];
    GP[GC] = { mRow, mCol, mCategory, -BW[y][x], mTime, -1, h };
    if (h != -1) GP[h].p = GC;
    BH[y][x] = GC++; BA[y][x]++;
    return 1;
}
 
int water(int mTime, int Gv, int mRow, int mCol, int mHeight, int mWidth) {
    int by = mRow / BS, bx = mCol / BS, ey = (mRow + mHeight - 1) / BS, ex = (mCol + mWidth - 1) / BS, res = 0;
    FR(sy, by, ey) FR(sx, bx, ex) {
        int l = sy * BS, r = l + BS - 1, a = sx * BS, b = a + BS - 1;
        if (mRow <= l && mRow + mHeight - 1 >= r && mCol <= a && mCol + mWidth - 1 >= b) {
            BW[sy][sx] += Gv; res += BA[sy][sx];
        }
        else {
            int c = BH[sy][sx];
            WH(c) {
                if (II(GP[c].y, GP[c].x, RN)) { GP[c].s += Gv; ++res; }
                c = GP[c].n;
            }
        }
    }
    return res;
}
 
int harvest(int mTime, int L, int mRow, int mCol, int mHeight, int mWidth) {
    int by = mRow / BS, bx = mCol / BS, ey = (mRow + mHeight - 1) / BS, ex = (mCol + mWidth - 1) / BS, res = 0;
    FR(sy, by, ey) FR(sx, bx, ex) {
        int c = BH[sy][sx];
        WH(c) {
            if (II(GP[c].y, GP[c].x, RN)) {
                if (GS(mTime, GP[c].t, GP[c].c) + GP[c].s + BW[sy][sx] < L) return 0;
                ++res;
            }
            c = GP[c].n;
        }
    }
    if (!res) return 0;
    FR(sy, by, ey) FR(sx, bx, ex) {
        int c = BH[sy][sx];
        WH(c) {
            int nt = GP[c].n;
            if (II(GP[c].y, GP[c].x, RN)) {
                V[GP[c].y][GP[c].x] = 0; BA[sy][sx]--;
                int p = GP[c].p, n = GP[c].n;
                if (p != -1) GP[p].n = n; else BH[sy][sx] = n;
                if (n != -1) GP[n].p = p;
            }
            c = nt;
        }
    }
    return res;
}