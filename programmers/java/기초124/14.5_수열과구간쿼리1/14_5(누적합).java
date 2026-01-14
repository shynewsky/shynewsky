class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        // int[] answer = {};
        // return answer;
        int n = arr.length;
        int[] diff = new int[n+1];

        for (int[] q : queries) {
            int s = q[0], e = q[1];
            diff[s] += 1;
            diff[e+1] -= 1;
        }

        int add = 0;
        for (int i = 0; i < n; i++) {
            add += diff[i];
            arr[i] += add;
        }

        return arr;
    }
}