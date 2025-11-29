#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;
    
    // 코드입력
    // int끼리 나눠도 소숫점 안나오기 때문에, float형으로 바꾼 후 나눠야한다
    answer = (int)(((float)num1 / (float)num2) * 1000);

    return answer;
}
 

