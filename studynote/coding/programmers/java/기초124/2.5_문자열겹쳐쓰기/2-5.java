class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        // String answer = "";
        // return answer;
        //////////////////////////////////////
        String front = my_string.substring(0, s); // 인덱스 s부터 overwrite_string의 길이만큼
        String back = my_string.substring(s + overwrite_string.length()); // overwrite_string으로 바꾼 문자열
        return front + overwrite_string + back;
        //////////////////////////////////////
    }
}