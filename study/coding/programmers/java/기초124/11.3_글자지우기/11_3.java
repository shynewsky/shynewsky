class Solution {
    public String solution(String my_string, int[] indices) {
        // String answer = "";
        // return answer;
        //////////////////////////////////////
        boolean[] remove = new boolean[my_string.length()];
        for (int idx : indices) {
            remove[idx] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < my_string.length(); i++) {
            if (!remove[i]) {
                sb.append(my_string.charAt(i));
            }
        }

        return sb.toString();
        //////////////////////////////////////
    }
}