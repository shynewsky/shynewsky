import java.math.BigInteger;

class Solution {
    public String solution(String a, String b) {
        // String answer = "";
        // return answer;
        BigInteger A = new BigInteger(a);
        BigInteger B = new BigInteger(b);
        return A.add(B).toString();
    }
}