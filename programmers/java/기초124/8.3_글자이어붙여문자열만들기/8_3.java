class Solution {
    public String solution(String my_string, int[] index_list) {
        // String answer = "";
        // return answer;
        //////////////////////////////////////
        StringBuilder sb = new StringBuilder();

        for (int idx : index_list) {
            sb.append(my_string.charAt(idx));
        }

        return sb.toString();
        //////////////////////////////////////
    }
}