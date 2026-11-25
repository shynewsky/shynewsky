class Solution {
    public int solution(int[] num_list) {
        // int answer = 0;
        int answer;
        if (num_list.length >= 11) {
            answer = 0;
            for (int x : num_list) {
                answer += x;
            }
        } else {
            answer = 1;
            for (int x : num_list) {
                answer *= x;
            }
        }
        return answer;
    }
}