#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    cout << a - b << endl;
    cout << a * b << endl;
    cout << a / b << endl;
    cout << a % b << endl;
    cout << fixed << setprecision(2) << static_cast<float>(a)/b;
    return 0;
}