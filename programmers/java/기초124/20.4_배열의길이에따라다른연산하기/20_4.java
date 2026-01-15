class Solution {
    public int[] solution(int[] arr, int n) {
        // int[] answer = {};
        // return answer;
        int len = arr.length;
        int start = (len % 2 == 1) ? 0 : 1;
        for (int i = start; i < len; i += 2) {
            arr[i] += n;
        }
        return arr;
    }
}