#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    double w, h, b;
    cin >> w >> h >> b;

    double ans = (w*h*b) / (8*1024*1024);
    cout << fixed << setprecision(2) << ans << " MB";
    return 0;
}