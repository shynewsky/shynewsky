import java.util.Arrays;

class Solution {
    public int solution(int a, int b, int c, int d) {
        // int answer = 0;
        // return answer;
        //////////////////////////////////////
        int[] x = {a, b, c, d};
        Arrays.sort(x); // x[0] <= x[1] <= x[2] <= x[3]

        // 4개 모두 같음
        if (x[0] == x[3]) return 1111 * x[0];

        // 3개 같음 (앞 3개 or 뒤 3개)
        if (x[0] == x[2]) { // p p p q
            int p = x[0], q = x[3];
            int v = 10 * p + q;
            return v * v;
        }
        if (x[1] == x[3]) { // q p p p
            int p = x[3], q = x[0];
            int v = 10 * p + q;
            return v * v;
        }

        // 2개+2개
        if (x[0] == x[1] && x[2] == x[3]) {
            int p = x[0], q = x[2];
            return (p + q) * Math.abs(p - q);
        }

        // 2개+1개+1개
        if (x[0] == x[1]) return x[2] * x[3];
        if (x[1] == x[2]) return x[0] * x[3];
        if (x[2] == x[3]) return x[0] * x[1];

        // 전부 다름
        return x[0];
        //////////////////////////////////////
    }
}