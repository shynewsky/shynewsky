class Solution {
    public String solution(String myString) {
        // String answer = "";
        // return answer;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < myString.length(); i++) {
            char c = myString.charAt(i);
            if (c < 'l') sb.append('l');
            else sb.append(c);
        }

        return sb.toString();

    }
}