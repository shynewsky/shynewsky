class Solution {
    public int[] solution(int[] num_list, int n) {
        // int[] answer = {};
        int len = num_list.length;
        int[] answer = new int[len];
        int idx = 0;

        // n번쨰 이후 원소들
        for (int i = n; i < len; i++) {
            answer[idx++] = num_list[i];
        }

        // n번째까지의 원소들
        for (int i = 0; i < n; i++) {
            answer[idx++] = num_list[i];
        }
        
        return answer;
    }
}