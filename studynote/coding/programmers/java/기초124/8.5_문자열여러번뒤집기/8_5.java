class Solution {
    public String solution(String my_string, int[][] queries) {
        // String answer = "";
        // return answer;
        //////////////////////////////////////
        char[] arr = my_string.toCharArray();

        for (int[] q : queries) {
            int s = q[0];
            int e = q[1];

            while (s < e) {
                char tmp = arr[s];
                arr[s] = arr[e];
                arr[e] = tmp;
                s++;
                e--;
            }
        }
        
        return new String(arr);
        //////////////////////////////////////
    }
}