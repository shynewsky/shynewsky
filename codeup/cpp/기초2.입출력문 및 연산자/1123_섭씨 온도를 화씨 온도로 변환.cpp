#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int a;
    cin >> a;
    cout << fixed << setprecision(3) << static_cast<float>(9)/5*a+32;
    return 0;
}