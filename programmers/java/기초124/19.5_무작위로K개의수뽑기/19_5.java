import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        // int[] answer = {};
        // return answer;
        int[] answer = new int[k];
        Arrays.fill(answer, -1);

        Set<Integer> seen = new HashSet<>();
        int idx = 0;

        for (int x : arr) {
            if (seen.add(x)) {
                answer[idx++] = x;
                if (idx == k) break;
            }
        }

        return answer;
    }
}