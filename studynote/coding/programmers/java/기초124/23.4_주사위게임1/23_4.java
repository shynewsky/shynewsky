class Solution {
    public int solution(int a, int b) {
        // int answer = 0;
        // return answer;
        boolean aOdd = (a % 2 == 1);
        boolean bOdd = (b % 2 == 1);

        if (aOdd && bOdd) {
            return a * a + b * b;
        } else if (aOdd || bOdd) {
            return 2 * (a + b);
        } else {
            return Math.abs(a-b);
        }
    }
}