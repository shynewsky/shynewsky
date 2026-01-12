class Solution {
    public int[] solution(int[] arr, int[] query) {
        // int[] answer = {};
        // return answer;
        //////////////////////////////////////
        int left = 0;
        int right = arr.length - 1;

        for (int i = 0; i < query.length; i++) {
            int q = query[i];

            if (i % 2 == 0) {
                right = left + q;
            } else {
                left = left + q;
            }
        }

        int[] answer = new int[right - left + 1];
        System.arraycopy(arr, left, answer, 0, answer.length);
        //////////////////////////////////////
        return answer;
    }
}