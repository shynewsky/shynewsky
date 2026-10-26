class Solution {
    public int[] solution(int[] arr) {
        // int[] answer = {};
        int n = arr.length;

        int p = 1;
        while (p < n) p <<= 1;

        int[] answer = new int[p];
        for (int i = 0; i < n; i++) {
            answer[i] = arr[i];
        }

        return answer;
    }
}