class Solution {
    public int[] solution(int[] num_list, int n) {
        // int[] answer = {};
        int len = num_list.length;
        int[] answer = new int[len - (n - 1)];

        for (int i = n-1; i < len; i++) {
            answer[i - (n-1)] = num_list[i];
        }

        return answer;
    }
}