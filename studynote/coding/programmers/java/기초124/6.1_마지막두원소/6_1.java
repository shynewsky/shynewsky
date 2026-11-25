class Solution {
    public int[] solution(int[] num_list) {
        // int[] answer = {};
        //////////////////////////////////////
        int len = num_list.length;
        int[] answer = new int[len+1]; // 길이 하나 더 큰 배열

        System.arraycopy(num_list, 0, answer, 0, len);

        int last = num_list[len-1];
        int prev = num_list[len-2];

        answer[len] = last > prev ? last - prev : last * 2;
        //////////////////////////////////////
        return answer;
    }
}