class Solution {
    public int[] solution(int[] arr) {
        // int[] answer = {};
        // return answer;
        int[] answer = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            int x = arr[i];

            if (x >= 50 && x % 2 == 0) {
                answer[i] = x / 2;
            } else if (x < 50 && x % 2 == 1) {
                answer[i] = x * 2;
            } else {
                answer[i] = x;
            }
        }
        return answer;
    }
}