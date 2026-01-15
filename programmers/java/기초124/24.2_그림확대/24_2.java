class Solution {
    public String[] solution(String[] picture, int k) {
        // String[] answer = {};
        int h = picture.length;
        int w = picture[0].length();

        String[] answer = new String[h * k];
        int idx = 0;

        for (String row : picture) {
            // 1️⃣ 가로 k배 확대
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < w; i++) {
                for (int t = 0; t < k; t++) {
                    sb.append(row.charAt(i));
                }
            }
            String expandedRow = sb.toString();

            // 2️⃣ 세로 k배 확대
            for (int t = 0; t < k; t++) {
                answer[idx++] = expandedRow;
            }
        }

        return answer;

    }
}