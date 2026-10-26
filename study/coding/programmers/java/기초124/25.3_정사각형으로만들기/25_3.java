class Solution {
    public int solution(int[][] arr) {
        // int answer = 0;
        // return answer;
        int n = arr.length;
        for (int i = 0l i < n; i++) {
            for (int j = i + 1; j < n ; j++) {
                if (arr[i][j] != arr[j][i]) {
                    return 0;
                }
            }
        }
        return 1;
    }
}