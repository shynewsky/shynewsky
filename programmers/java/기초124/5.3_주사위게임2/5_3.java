class Solution {
    public int solution(int a, int b, int c) {
        // int answer = 0;
        // return answer;
        //////////////////////////////////////
        int sum1 = a + b + c;
        int sum2 = a*a + b*b + c*c;
        int sum3 = a*a*a + b*b*b + c*c*c;

        // 모두 같음
        if (a == b && b == c) {
            return sum1 * sum2 * sum3;
        }
        // 두개만 같음
        if (a == b || a == c || b == c) {
            return sum1 * sum2;
        }
        // 모두 다름
        return sum1;
        //////////////////////////////////////
    }
}