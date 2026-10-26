import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> list = new ArrayList<>();
        Queue<Long> q = new ArrayDeque<>();

        q.add(5L); // 0으로 시작하는 수는 불가능하므로 5부터 시작

        while (!q.isEmpty()) {
            long cur = q.poll();

            if (cur > r) continue;
            if (cur >= l) list.add((int) cur);

            // 다음 후보 생성: 뒤에 0 또는 5 붙이기
            long next0 = cur * 10;
            long next5 = cur * 10 + 5;

            if (next0 <= r) q.add(next0);
            if (next5 <= r) q.add(next5);
        }

        if (list.isEmpty()) return new int[]{-1};

        Collections.sort(list); // 생성 순서가 항상 정렬 보장은 아니라서 안전하게 정렬
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) answer[i] = list.get(i);
        return answer;
    }
}
