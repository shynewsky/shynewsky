#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int d = n%7;
    if (1<=d && d<=5) cout << "주중";
    else cout << "주말";
    return 0;
}