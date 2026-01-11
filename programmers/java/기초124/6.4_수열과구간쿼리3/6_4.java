class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        // int[] answer = {};
        // return answer;
        //////////////////////////////////////
        for (int[] q : queries) {
            int i = q[0];
            int j = q[1];

            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        return arr;
        //////////////////////////////////////
    }
}