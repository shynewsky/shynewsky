class Solution {
    public int solution(String myString, String pat) {
        // int answer = 0;
        // return answer;
        return myString.toLowerCase().contains(pat.toLowerCase()) ? 1 : 0;
    }
}