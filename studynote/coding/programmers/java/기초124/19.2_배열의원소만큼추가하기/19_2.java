import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        // int[] answer = {};
        List<Integer> list = new ArrayList<>();

        for (int a : arr) {
            for (int i = 0; i < a; i++) {
                list.add(a);
            }
        }

        // List → int[]
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}