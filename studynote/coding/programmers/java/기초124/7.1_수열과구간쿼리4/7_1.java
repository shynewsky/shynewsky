class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        // int[] answer = {};
        // return answer;
        //////////////////////////////////////
        for (int[] q : queries) {
            int s = q[0], e = q[1], k = q[2];

            if (k == 0) {
                if (s <= 0 && 0 <= e) arr[0] += 1;
                continue;
            }

            int start = ((s + k - 1) / k) * k;

            for (int i = start; i <= e; i += k) {
                arr[i] += 1;
            }
        }
        return arr;
        //////////////////////////////////////
    }
}