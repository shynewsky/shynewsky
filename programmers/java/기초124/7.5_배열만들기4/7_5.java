import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        // int[] stk = {};
        // return stk;
        //////////////////////////////////////
        Deque<Integer> stk = new ArrayDeque<>();
        int i = 0;

        while (i < arr.length) {
            if (stk.isEmpty()) {
                stk.push(arr[i]);
                i++;
            } else if (stk.peek() < arr[i]) {
                stk.push(arr[i]);
                i++;
            } else {
                stk.pop();
            }
        }

        int[] answer = new int[stk.size()];
        for (int idx = answer.length -1; idx >= 0; idx--) {
            answer[idx] = stk.pop();
        }

        return answer;
        //////////////////////////////////////
    }
}