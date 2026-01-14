class Solution {
    public int solution(int[] num_list) {
        int answer = 0;

        for (int x : num_list) {
            while (x > 1) {
                if (x % 2 == 0) {
                    x /= 2;
                } else {
                    x = (x - 1) / 2;
                }
                answer ++;
            }
        }

        return answer;
    }
}