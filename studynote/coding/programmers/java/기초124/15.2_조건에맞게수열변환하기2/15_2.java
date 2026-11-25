class Solution {
    public int solution(int[] arr) {
        int answer = 0;

        for (int x : arr) {
            int cnt = 0;

            while (true) {
                if (x >= 50 && x % 2 == 0) {
                    x /= 2;
                    cnt++;
                } else if (x < 50 && x % 2 == 1) {
                    x = x * 2 + 1;
                    cnt++;
                } else {
                    break; // 더 이상 변하지 않는 상태
                }
            }

            if (cnt > answer) answer = cnt;
        }

        return answer;
    }
}
