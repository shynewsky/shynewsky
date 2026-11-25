class Solution {
    public int solution(int[] numbers, int n) {
        int answer = 0;

        for (int x : numbers) {
            answer += x;
            if (answer > n) {
                return answer;
            }
        }

        return answer;
    }
}