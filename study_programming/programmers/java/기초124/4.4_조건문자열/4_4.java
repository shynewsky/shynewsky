class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        // int answer = 0;
        // return answer;
        //////////////////////////////////////
        String op = ineq + eq;

        if (op.equals(">=")) return n >= m ? 1 : 0;
        if (op.equals("<=")) return n <= m ? 1 : 0;
        if (op.equals(">!")) return n > m ? 1 : 0;
        if (op.equals("<!")) return n < m ? 1 : 0;

        return 0; // ⭐ Java 는 모든 경우에 return 이 붙어야 한다.
        //////////////////////////////////////
    }
}