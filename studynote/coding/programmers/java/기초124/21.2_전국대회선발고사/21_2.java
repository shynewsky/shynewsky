import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        // int answer = 0;
        // return answer;
        List<int[]> candidates = new ArrayList<>();
        for (int i = 0; i < rank.length; i++) {
            if (attendance[i]) {
                candidates.add(new int[]{rank[i], i});
            }
        }
        candidates.sort((x, y) -> x[0] - y[0]);
        int a = candidates.get(0)[1];
        int b = candidates.get(1)[1];
        int c = candidates.get(2)[1];

        return 10000 * a + 100 * b + c;
    }
}