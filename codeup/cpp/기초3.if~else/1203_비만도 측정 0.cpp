#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    if (n <= 10) cout << "정상";
    else if (n <= 20) cout << "과체중";
    else cout << "비만";
    return 0;
}