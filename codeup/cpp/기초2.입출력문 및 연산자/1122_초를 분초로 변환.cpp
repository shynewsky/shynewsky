#include <iostream>
using namespace std;

int main(){
    int a;
    cin >> a;
    cout << static_cast<int>(a/60) << " " << a % 60;
    return 0;
}