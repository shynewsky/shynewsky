import java.util.*;

class Solution {
    public String[] solution(String myStr) {
        // String[] answer = {};
        // return answer;
        // a, b, c를 모두 구분자로 사용
        String[] parts = myStr.split("[abc]");
        List<String> list = new ArrayList<>();

        // 빈 문자열 제거
        for (String s : parts) {
            if (!s.isEmpty()) {
                list.add(s);
            }
        }

        // 결과가 비어 있으면 ["EMPTY"]
        if (list.isEmpty()) {
            return new String[] {"EMPTY"};
        }

        return list.toArray(new String[0]);
    }
}