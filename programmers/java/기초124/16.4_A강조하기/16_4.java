class Solution {
    public String solution(String myString) {
        // String answer = "";
        // return answer;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < myString.length(); i++) {
            char c = myString.charAt(i);

            if (c == 'a') {
                sb.append('A');                 // a -> A
            } else if (c == 'A') {
                sb.append('A');                 // A는 그대로
            } else if (c >= 'A' && c <= 'Z') {
                sb.append((char)(c - 'A' + 'a'));// 다른 대문자 -> 소문자
            } else {
                sb.append(c);                   // 그 외(소문자 등) 그대로
            }
        }

        return sb.toString();
    }
}