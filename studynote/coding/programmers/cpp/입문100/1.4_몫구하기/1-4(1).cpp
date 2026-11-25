#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;
    
    // 코드입력
    // 나머지를 구하는 것은 % 연산이지만, 몫을 구하는 연산자는 없다
    // 나머지를 뺀 후 나누면 0으로 나누어 떨어진다
    // 소숫점이 나오지 않기 때문에, 반올림하거나 소수점 아래를 구해서 뺄 필요가 없다
    answer = (num1 - (num1 % num2)) / num2 ;

    return answer;
}
