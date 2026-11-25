class Solution {
    public int solution(String myString, String pat) {
        // int answer = 0;
        // return answer;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < myString.length(); i++) {
            char c = myString.charAt(i);
            sb.append(c == 'A' ? 'B' : 'A');
        }

        return sb.toString().contains(pat) ? 1 : 0;
    }
}