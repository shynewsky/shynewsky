#include <iostream>
using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;

    int ans = (a < b ? a : b);
    ans = (ans < c ? ans : c);

    cout << ans;
    return 0;
}