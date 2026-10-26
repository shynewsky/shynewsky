class Solution {
    public int[] solution(int[] arr) {
        // int[] answer = {};
        // return answer;
        //////////////////////////////////////
        int first = -1;
        int last = -1;

        for (int i = 0; i < arr.length; i++){
            if (arr[i] == 2) {
                if (first == -1) first = i;
                last = i;
            }
        }

        if (first == -1) {
            return new int[]{-1};
        }

        int[] answer = new int[last - first + 1];
        System.arraycopy(arr, first, answer, 0, answer.length);
        //////////////////////////////////////
        return answer;
    }
}