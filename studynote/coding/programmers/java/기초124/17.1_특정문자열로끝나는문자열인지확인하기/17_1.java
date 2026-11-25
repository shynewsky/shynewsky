class Solution {
    public String solution(String myString, String pat) {
        // String answer = "";
        // return answer;
        int idx = myString.lastIndexOf(pat);
        return myString.substring(0, idx + pat.length());
    }
}