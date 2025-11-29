#include <string>
#include <vector>

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;

    // 코드입력
    // 약분없이 곱셈을 사용하여 분수의 합을 구한다
    int numer = (numer1 * denom2) + (numer2 * denom1);
    int denum = denom1 * denom2;

    // 최대공약수를 구하여 분모분자를 약분한다 (유클리드 호제법)
    int a = numer;
    int b = denum;
    int c;
    
    while(b != 0)
    {
        c = a % b;
        a = b;
        b = c;
    }
    
    int gcd = a;

    // 최대공약수로 약분하기
    numer /= gcd;
    denum /= gcd;
    
    // 벡터에 분자 분모 순서대로 푸쉬백한다        
    answer.push_back(numer);
    answer.push_back(denum);

    return answer;
}
