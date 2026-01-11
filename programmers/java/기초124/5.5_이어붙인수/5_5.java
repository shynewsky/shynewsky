class Solution {
    public int solution(int[] num_list) {
        // int answer = 0;
        // return answer;
        //////////////////////////////////////
        StringBuilder odd = new StringBuilder();
        StringBuilder even = new StringBuilder();

        for (int n : num_list) {
            if (n % 2 == 0) {
                even.append(n);
            } else {
                odd.append(n);
            }
        }

        int oddNum = Integer.parseInt(odd.toString());
        int evenNum = Integer.parseInt(even.toString());

        return oddNum + evenNum;
        //////////////////////////////////////
    }
}