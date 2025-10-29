#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    // float 는 소수점 이하를 정확하게 처리하지 못하므로 double 사용
    double a, b;
    cin >> a >> b;
    if (a > b){
        double c = a;
        a = b;
        b = c;
    }
    for (double i = a; i <= b; i += 0.01){
        cout << fixed << setprecision(2) << i << ' ';
    }
    return 0;
}