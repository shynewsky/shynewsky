import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        // int[] answer = {};
        // return answer;
        //////////////////////////////////////
        List<Integer> list = new ArrayList<>();

        for (String str : intStrs) {
            int val = Integer.parseInt(str.substring(s, s + l));
            if (val > k) list.add(val);
        }

        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        //////////////////////////////////////
        return answer;
    }
}