class Solution {
    public int solution(int a, int b) {
        // int answer = 0;
        // return answer;
        //////////////////////////////////////
        String ab = String.valueOf(a) + b;
        String ba = String.valueOf(b) + a;

        int val1 = Integer.parseInt(ab);
        int val2 = Integer.parseInt(ba);

        return val1 >= val2 ? val1 : val2;
        //////////////////////////////////////
    }
}