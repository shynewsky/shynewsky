class Solution {
    public int[] solution(int[] arr) {
        // int[] answer = {};
        int n = arr.length;
        int[] stack = new int[n];
        int top = 0;

        for (int i = 0; i < n; i++) {
            int x = arr[i];

            if (top == 0) {
                stack[top++] = x;
            } else if (stack[top-1] == x) {
                top--;
            } else {
                stack[top++] = x;
            }
        }

        if (top == 0) return new int[] { -1 };

        int[] answer = new int[top];
        for (int i = 0; i < top; i++) {
            answer[i] = stack[i];
        }

        return answer;
    }
}