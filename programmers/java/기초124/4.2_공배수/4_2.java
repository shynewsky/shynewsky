class Solution {
    public int solution(int number, int n, int m) {
        // int answer = 0;
        // return answer;
        //////////////////////////////////////
        return (number % n == 0 && number % m == 0) ? 1 : 0;
        //////////////////////////////////////
    }
}