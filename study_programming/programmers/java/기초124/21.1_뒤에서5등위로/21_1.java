import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        // int[] answer = {};
        // return answer;
        Arrays.sort(num_list);
        return Arrays.copyOfRange(num_list, 5, num_list.length);
    }
}