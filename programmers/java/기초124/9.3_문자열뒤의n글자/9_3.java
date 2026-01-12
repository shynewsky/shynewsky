class Solution {
    public String solution(String my_string, int n) {
        // String answer = "";
        // return answer;
        //////////////////////////////////////
        int start = my_string.length() - n;
        return my_string.substring(start);
        //////////////////////////////////////
    }
}