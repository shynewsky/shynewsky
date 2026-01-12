class Solution {
    public int[] solution(String my_string) {
        // int[] answer = {};
        //////////////////////////////////////
        int[] answer = new int[52];

        for (int i = 0; i < my_string.length(); i++) {
            char ch = my_string.charAt(i);

            if (ch >= 'A' && ch <= 'Z') {
                answer[ch - 'A']++;
            } else {
                answer[ch - 'a' + 26]++;
            }
        }
        //////////////////////////////////////
        return answer;
    }
}