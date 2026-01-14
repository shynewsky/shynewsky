import java.util.*;

class Solution {
    public int solution(String binomial) {
        // int answer = 0;
        // return answer;
        String[] parts = binomial.split(" ");
        int a = Integer.parseInt(parts[0]);
        String op = parts[1];
        int b = Integer.parseInt(parts[2]);

        if (op.equals("+")) {
            return a + b;
        } else if (op.equals("-")) {
            return a - b;
        } else { // "*"
            return a * b;
        }
    }
}