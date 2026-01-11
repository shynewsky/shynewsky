class Solution {
    public int solution(int[] num_list) {
        // int answer = 0;
        // return answer;
        //////////////////////////////////////
        long sum = 0;
        long prod = 1;

        for (int x : num_list) {
            sum += x;
            prod *= x;
        }

        return prod < sum * sum ? 1 : 0;
        //////////////////////////////////////
    }
}