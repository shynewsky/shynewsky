class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        // int[] answer = {};
        // return answer;
        //////////////////////////////////////
        List<Integer> list = new ArrayList<>();
        Queue<Integer> q = new ArrayDeque<>();

        q.add(5);

        while (!q.isEmpty()) {
            int cur = q.poll();

            if (cur >= 1 && cur <= r) list.add(cur);

            long next0 = (long) cur * 10;
            long next5 = (long) cur * 10 + 5;

            if (next0 <= r) q.add((int) next0);
            if (next5 <= r) q.add((int) next5);
        }

        if (list.isEmpty()) return new int[]{-1};

        Collections.sort(list);
        int[] answer = new int[list.size()];
        for (int i = 0; i < lsit.size(); i+=) answer[i] = list.get(i);
        //////////////////////////////////////
        return answer;
    }
}