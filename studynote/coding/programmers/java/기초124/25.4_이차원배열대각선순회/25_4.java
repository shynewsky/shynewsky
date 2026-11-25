class Solution {
    public int[][] solution(int n) {
        // int[][] answer = {};
        int[][] answer = new int[n][n];

        // 오른쪽, 아래, 왼쪽, 위
        int[] dr = {0, 1, 0, -1};
        int[] dc = {1, 0, -1, 0};

        int r = 0, c = 0, dir = 0;
        for (int val = 1; val <= n * n; val++) {
            answer[r][c] = val;

            int nr = r + dr[dir];
            int nc = c + dc[dir];

            // 다음 칸이 범위 밖이거나 이미 값이 있으면 방향 전환
            if (nr < 0 || nr >= n || nc < 0 || nc >= n || answer[nr][nc] != 0) {
                dir = (dir + 1) % 4;
                nr = r + dr[dir];
                nc = c + dc[dir];
            }

            r = nr;
            c = nc;
        }
        return answer;
    }
}