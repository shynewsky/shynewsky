#include <iostream>

using namespace std;

int main(void) {
    int a;
    int c;
    cin >> a >> c;
    
    // int b_square = c - a;
    // cout << b_square << endl;

    // 제곱을 ^2로 계산하는 것이 아닌, 스스로를 곱해야한다
    int b_square = c*c - a*a;

    return 0;
}
