#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    
    // 코드입력
    for (int i : numbers)
        answer.push_back(i * 2);

    return answer;
}
