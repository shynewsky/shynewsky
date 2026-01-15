import java.util.*;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        // int[] answer = {};
        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            int a = arr[i];

            if (flag[i]) {
                // a를 a*2번 추가
                for (int k = 0; k < a * 2; k++) {
                    list.add(a);
                }
            } else {
                // 뒤에서 a개 제거
                for (int k = 0; k < a; k++) {
                    list.remove(list.size() - 1);
                }
            }
        }

        // List -> int[]
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}
