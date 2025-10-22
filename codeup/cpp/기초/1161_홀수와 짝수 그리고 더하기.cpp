#include <iostream>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    if (a % 2 == 1) cout << "홀수";
    else cout << "짝수";
    cout << "+";
    if (b % 2 == 1) cout << "홀수";
    else cout << "짝수";
    cout << "=";
    if ((a+b) % 2 == 1) cout << "홀수";
    else cout << "짝수";
    return 0;
}