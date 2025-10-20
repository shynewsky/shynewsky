#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    double h, b, c, s;
    cin >> h >> b >> c >> s;

    double ans = (h*b*c*s) / (8*1024*1024);
    cout << fixed << setprecision(1) << ans << " MB";
    return 0;
}