class Solution {
    public int solution(int a, int b) {
        // int answer = 0;
        // return answer;
        //////////////////////////////////////
        int concat = Integer.parseInt(String.valueOf(a) + b);
        int multiply = 2 * a * b;

        return concat >= multiply ? concat : multiply;
        //////////////////////////////////////
    }
}