class Solution {
    public int solution(String[] strArr) {
        // int answer = 0;
        // return answer;
        int[] cnt = new int[31];
        int max = 0;

        for (String s : strArr) {
            int len = s.length();
            int c = ++cnt[len];
            if (c > max) max = c;
        }

        return max;
    }
}