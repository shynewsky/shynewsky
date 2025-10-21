#include <iostream>
using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    int d = (a < b ? a : b);
    cout << (d < c ? d : c);
    return 0;
}
