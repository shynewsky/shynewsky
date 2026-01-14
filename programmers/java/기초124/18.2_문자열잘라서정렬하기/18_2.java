import java.util.*;

class Solution {
    public String[] solution(String myString) {
        // String[] answer = {};
        // return answer;
        String[] parts = myString.split("x");
        List<String> list = new ArrayList<>();

        // 빈 문자열 제거
        for (String s : parts) {
            if (!s.isEmpty()) {
                list.add(s);
            }
        }

        // 사전순 정렬
        Collections.sort(list);

        // 배열로 변환
        return list.toArray(new String[0]);
    }
}