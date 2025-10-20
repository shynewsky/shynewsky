#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    cout << fixed << setprecision(2) << static_cast<float>(a+b+c)/3;
    return 0;
}