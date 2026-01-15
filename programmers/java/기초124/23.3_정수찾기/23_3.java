class Solution {
    public int solution(int[] num_list, int n) {
        // int answer = 0;
        // return answer;
        for (int x : num_list) {
            if (x == n) {
                return 1;
            }
        }
        return 0;
    }
}