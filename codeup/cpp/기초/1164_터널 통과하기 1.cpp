#include <iostream>
using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    if ((a > 170) && (b > 170) && (c > 170)) cout << "PASS";
    else cout << "CRASH";
    return 0;
}