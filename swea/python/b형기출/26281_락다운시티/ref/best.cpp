/*
보안 등급의 최대 길이가 3이므로 26진법으로 나타내면 각 셀의 보안 등급을 정수로 저장할 수 있음
 
change 쉽고 calculate는 max-min 문제인데, 이분 탐색 + 격자 그래프 BFS로 하면 될 듯
 
이제 "A"부터 "ZZZ"까지 사전 순으로 매핑해야 하는데, "A" = 0, "AA" = 1, "AAA" = 2 등등
 
이걸 어떻게 할 거냐? 최대 길이가 3이잖아. 문자열 벡터를 만들고 조합을 다 넣은 다음에 정렬하면 되지. 26 + 26^2 + 26^3 = 18,278개
 
최대 O(N^2) BFS를 15번(log_2(18,278))
 
시간 개선 1) 단방향 BFS -> 양방향 BFS
 
시간 개선 2) 방문 배열 도입, 추가 초기화 X
 
시간 개선 3) 정적 배열 도입
 
시간 개선 4) 정적 배열 큐 도입
*/
 
#define MAX_M 4
#define MAX_N 100
 
#include <vector>
#include <queue>
#include <cctype>
#include <string>
#include <algorithm>
#include <unordered_map>
 
#include <iostream>
 
struct State {
    int r, c;
};
 
int board[MAX_N][MAX_N];
 
// 시작점에서부터 거리, 도착점에서부터 거리, 각각 방문 처리
int distS[MAX_N][MAX_N];
int distE[MAX_N][MAX_N];
int visS[MAX_N][MAX_N];
int visE[MAX_N][MAX_N];
 
std::vector<std::string> str_vec; // 사전순 번호 -> 문자열
std::unordered_map<std::string, int> str_to_order; // 문자열 -> 사전순 번호
 
int dr[4] = {1, 0, -1, 0};
int dc[4] = {0, 1, 0, -1};
 
int NN, MM;
 
int visit_cnt = 0;
 
constexpr int INF = (1 << 20);
 
void init(int N, int M, char mGrade[][MAX_N][MAX_M]) {
    NN = N;
    MM = M;
     
    if (str_vec.empty()) {
        str_vec.reserve(18'300);
        for (char i = 'A'; i <= 'Z'; i++) {
            str_vec.emplace_back(std::string(1, i));
        }
 
        for (char i = 'A'; i <= 'Z'; i++) {
            for (char j = 'A'; j <= 'Z'; j++) {
                std::string concat;
                concat += i;
                concat += j;
                str_vec.emplace_back(concat);
            }
        }
 
        for (char i = 'A'; i <= 'Z'; i++) {
            for (char j = 'A'; j <= 'Z'; j++) {
                for (char k = 'A'; k <= 'Z'; k++) {
                    std::string concat;
                    concat += i;
                    concat += j;
                    concat += k;
                    str_vec.emplace_back(concat);
                }
            }
        }
 
        std::sort(str_vec.begin(), str_vec.end());
        for (int i = 0; i < str_vec.size(); i++) {
            str_to_order[str_vec[i]] = i;
        }
    }
 
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            std::string str = mGrade[r][c];
            board[r][c] = str_to_order[str];
        }
    }
}
 
void change(int mRow, int mCol, int mDir, int mLength, char mGrade[MAX_M]) {
    std::string str = mGrade;
    for (int d = 0; d < mLength; d++) {
        int r = mRow + dr[mDir] * d;
        int c = mCol + dc[mDir] * d;
 
         
        board[r][c] = str_to_order[str];
    }
}
 
char ret[MAX_M];
char* calculate(int L, int sRow, int sCol, int eRow, int eCol) {
 
    int lo = 0; // "A"
    int hi = 26 * 26 * 26 + 26 * 26 + 26 - 1; // "ZZZ"까지의 개수
    int ans = -1;
 
    while (lo <= hi) {
        visit_cnt++;
 
        int mid = lo + (hi - lo) / 2; // 경로 상의 모든 수가 mid 이상인 경로를 찾을 수 있는가? 가능하면 범위를 큰 쪽으로, 불가능하면 작은 쪽으로
 
        State qS[MAX_N * MAX_N];
        State qE[MAX_N * MAX_N];
        int headS = 0, tailS = 0, headE = 0, tailE = 0;
 
        qS[tailS++] = { sRow, sCol };
        qE[tailE++] = { eRow, eCol };
 
        distS[sRow][sCol] = distE[eRow][eCol] = 0;
        visS[sRow][sCol] = visE[eRow][eCol] = visit_cnt;
 
        bool ok = false;
 
        // 애초에 도착 칸을 못 가는 경우 컷
        if (board[eRow][eCol] < mid) {
            hi = mid - 1;
            continue;
        }
 
        while ((headS < tailS) && (headE < tailE)) {
            int sz1 = tailS - headS;
            while (sz1--) {
                auto [cr, cc] = qS[headS++];
                 
                int dist = distS[cr][cc];
 
                // 다 빼야 됨
                if (dist >= L) {
                    continue;
                }
 
                for (int dir = 0; dir < 4; dir++) {
                    int nr = cr + dr[dir];
                    int nc = cc + dc[dir];
 
                    if (nr < 0 || nr >= NN || nc < 0 || nc >= NN) {
                        continue;
                    }
 
                    if (board[nr][nc] < mid || visS[nr][nc] == visit_cnt) {
                        continue;
                    }
 
                    distS[nr][nc] = dist + 1;
                    visS[nr][nc] = visit_cnt;
                    qS[tailS++] = { nr, nc };
 
                    if (visE[nr][nc] == visit_cnt && distS[nr][nc] + distE[nr][nc] <= L) {
                        ok = true;
                        break;
                    }
                }
 
                if (ok) {
                    break;
                }
            }
 
            if (ok) {
                break;
            }
 
            int sz2 = tailE - headE;
            while (sz2--) {
                auto [cr, cc] = qE[headE++];
 
                int dist = distE[cr][cc];
 
                // 다 빼야 됨
                if (dist >= L) {
                    continue;
                }
 
                for (int dir = 0; dir < 4; dir++) {
                    int nr = cr + dr[dir];
                    int nc = cc + dc[dir];
 
                    if (nr < 0 || nr >= NN || nc < 0 || nc >= NN) {
                        continue;
                    }
                     
                    // 시작 칸은 mid와의 대소관계를 고려하지 않아야 하므로 그냥 넣기
                    if (!(nr == sRow && nc == sCol) && (board[nr][nc] < mid || visE[nr][nc] == visit_cnt)) {
                        continue;
                    }
 
                    distE[nr][nc] = dist + 1;
                    visE[nr][nc] = visit_cnt;
                    qE[tailE++] = { nr, nc };
 
                    if (visS[nr][nc] == visit_cnt && distS[nr][nc] + distE[nr][nc] <= L) {
                        ok = true;
                        break;
                    }
                }
 
                if (ok) {
                    break;
                }
            }
 
            if (ok) {
                break;
            }
        }
         
        if (ok) {
            ans = mid;
            lo = mid + 1;
        }
        else {
            hi = mid - 1;
        }
    }
 
    std::string ans_str = str_vec[ans];
    for (int i = 0; i < MAX_M; i++) {
        if (ans_str.size() > i) {
            ret[i] = ans_str[i];
        }
        else {
            ret[i] = '\0';
        }
    }
 
    return ret;
}