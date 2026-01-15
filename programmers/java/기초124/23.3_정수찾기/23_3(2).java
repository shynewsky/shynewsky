import java.util.Arrays;

class Solution {
    public int solution(int[] num_list, int n) {
        // int answer = 0;
        // return answer;
        return Arrays.stream(num_list).anyMatch(x -> x == n) ? 1 : 0;
    }
}