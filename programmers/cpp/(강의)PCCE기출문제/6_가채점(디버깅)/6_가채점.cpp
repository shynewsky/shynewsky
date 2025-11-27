#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<int> numbers, vector<int> our_score, vector<int> score_list) {
    int num_student = numbers.size();
    vector<string> answer(num_student);
    
    for (int i = 0; i < num_student; i++) {
        if (our_score[i] == score_list[numbers[i]-1]) {
        // 학생수를 번호로 순서로 가져가는 것이 아니라, 학생번호를 순서로 가져가야한다
            answer[i] = "Same";
        }
        else {
            answer[i] = "Different";
        }
    }
    
    return answer;
}
