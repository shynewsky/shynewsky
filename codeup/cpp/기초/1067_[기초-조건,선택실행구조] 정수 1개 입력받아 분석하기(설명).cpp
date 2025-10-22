#include <iostream>
using namespace std;

int main(){
    int a;
    cin >> a;
    if (a < 0) cout << "minus" << "\n";
    else cout << "plus" << "\n";
    if (a % 2 == 0) cout << "even" << "\n";
    else cout << "odd" << "\n";
    return 0;
}