class Solution {
    public int solution(int[] arr1, int[] arr2) {
        // int answer = 0;
        // return answer;
        // 1. 길이 비교
        if (arr1.length > arr2.length) return 1;
        if (arr1.length < arr2.length) return -1;

        // 2. 합 비교
        int sum1 = 0, sum2 = 0;
        for (int x : arr1) sum1 += x;
        for (int x : arr2) sum2 += x;

        if (sum1 > sum2) return 1;
        if (sum1 < sum2) return -1;

        // 3. 완전히 같음
        return 0;
    }
}